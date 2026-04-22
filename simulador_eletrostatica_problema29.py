"""Simulador interativo do Problema 29 (Fig. 21-32).

Cenário:
- Partículas 2 e 4: carga -e, fixas no eixo y em y2=-10 cm e y4=+5 cm.
- Partículas 1 e 3: carga -e, móveis no eixo x.
- Partícula 5: carga +e, fixa na origem.

Objetivo didático:
- Explorar como a força resultante sobre a partícula 1 muda conforme x1 e x3.
- Encontrar o valor de x3 para anular a força vertical (Fy=0),
  com x1=-10 cm fixo (item a).
- Verificar o deslocamento de x3 para que a direção da força resultante
  sobre a partícula 1 gire +30° em relação à direção original (item b).
"""

from __future__ import annotations

import math
import tkinter as tk
from dataclasses import dataclass


CM_TO_M = 0.01
COULOMB_CONST = 8.9875517923e9
E_CHARGE = 1.602176634e-19


@dataclass
class Vetor2D:
    x: float
    y: float

    @property
    def mod(self) -> float:
        return math.hypot(self.x, self.y)

    @property
    def ang_deg(self) -> float:
        return math.degrees(math.atan2(self.y, self.x))


def forca_de_q_em_p(
    xp_cm: float,
    yp_cm: float,
    xq_cm: float,
    yq_cm: float,
    qp: float,
    qq: float,
) -> Vetor2D:
    """Força elétrica em P causada por Q, usando unidades SI internamente."""
    rx = (xp_cm - xq_cm) * CM_TO_M
    ry = (yp_cm - yq_cm) * CM_TO_M
    r2 = rx * rx + ry * ry
    r = math.sqrt(r2)

    if r == 0:
        return Vetor2D(0.0, 0.0)

    f_mod = COULOMB_CONST * abs(qp * qq) / r2

    if qp * qq > 0:
        sinal = 1.0
    else:
        sinal = -1.0

    return Vetor2D(sinal * f_mod * rx / r, sinal * f_mod * ry / r)


def soma_forcas_sobre_particula_1(x1_cm: float, x3_cm: float) -> Vetor2D:
    """Soma das forças na partícula 1 (q1=-e) devido a 2,3,4,5."""
    q_neg = -E_CHARGE
    q_pos = +E_CHARGE

    fx = fy = 0.0

    for xq, yq, qq in [
        (0.0, -10.0, q_neg),  # partícula 2
        (x3_cm, 0.0, q_neg),  # partícula 3
        (0.0, +5.0, q_neg),   # partícula 4
        (0.0, 0.0, q_pos),    # partícula 5
    ]:
        f = forca_de_q_em_p(x1_cm, 0.0, xq, yq, q_neg, qq)
        fx += f.x
        fy += f.y

    return Vetor2D(fx, fy)


def achar_x3_para_fy_zero(x1_cm: float) -> float | None:
    """Busca numérica simples por x3 tal que Fy≈0 (com x1 fixo)."""
    melhor_x = None
    melhor_abs_fy = float("inf")

    for i in range(-3000, 3001):
        x3 = i / 100.0
        if abs(x3 - x1_cm) < 0.01:
            continue
        fy = soma_forcas_sobre_particula_1(x1_cm, x3).y
        if abs(fy) < melhor_abs_fy:
            melhor_abs_fy = abs(fy)
            melhor_x = x3

    if melhor_x is None:
        return None

    if melhor_abs_fy < 1e-18:
        return melhor_x
    return melhor_x


def achar_x3_para_rotacao(
    x1_cm: float,
    angulo_alvo_deg: float,
    x3_base_cm: float,
) -> float | None:
    """Acha x3 para que o ângulo da força mude em +angulo_alvo_deg."""
    f0 = soma_forcas_sobre_particula_1(x1_cm, x3_base_cm)
    ang0 = f0.ang_deg
    alvo = ang0 + angulo_alvo_deg

    melhor_x = None
    melhor_erro = float("inf")

    for i in range(-3000, 3001):
        x3 = i / 100.0
        if abs(x3 - x1_cm) < 0.01:
            continue
        ang = soma_forcas_sobre_particula_1(x1_cm, x3).ang_deg
        erro = abs((ang - alvo + 180.0) % 360.0 - 180.0)
        if erro < melhor_erro:
            melhor_erro = erro
            melhor_x = x3

    return melhor_x


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Simulador Interativo - Eletrostática (Problema 29)")
        self.geometry("980x680")

        self.x1_var = tk.DoubleVar(value=-10.0)
        self.x3_var = tk.DoubleVar(value=10.0)

        self._criar_layout()
        self.atualizar()

    def _criar_layout(self) -> None:
        frame_controles = tk.Frame(self)
        frame_controles.pack(side=tk.LEFT, fill=tk.Y, padx=12, pady=12)

        tk.Label(frame_controles, text="Controles", font=("Arial", 12, "bold")).pack(anchor="w")

        tk.Label(frame_controles, text="x1 (cm), partícula 1").pack(anchor="w", pady=(10, 2))
        tk.Scale(
            frame_controles,
            from_=-20,
            to=0,
            resolution=0.1,
            orient="horizontal",
            variable=self.x1_var,
            command=lambda _v: self.atualizar(),
            length=260,
        ).pack(anchor="w")

        tk.Label(frame_controles, text="x3 (cm), partícula 3").pack(anchor="w", pady=(10, 2))
        tk.Scale(
            frame_controles,
            from_=0,
            to=25,
            resolution=0.1,
            orient="horizontal",
            variable=self.x3_var,
            command=lambda _v: self.atualizar(),
            length=260,
        ).pack(anchor="w")

        tk.Button(
            frame_controles,
            text="Resolver item (a): Fy = 0",
            command=self.resolver_item_a,
            width=30,
        ).pack(anchor="w", pady=(14, 4))

        tk.Button(
            frame_controles,
            text="Resolver item (b): rotação +30°",
            command=self.resolver_item_b,
            width=30,
        ).pack(anchor="w", pady=4)

        tk.Button(
            frame_controles,
            text="Voltar para valores iniciais",
            command=self.resetar,
            width=30,
        ).pack(anchor="w", pady=4)

        self.lbl_info = tk.Label(
            frame_controles,
            justify="left",
            font=("Consolas", 10),
            text="",
            padx=6,
            pady=8,
        )
        self.lbl_info.pack(anchor="w", pady=(14, 0))

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=12, pady=12)

    def resetar(self) -> None:
        self.x1_var.set(-10.0)
        self.x3_var.set(10.0)
        self.atualizar()

    def resolver_item_a(self) -> None:
        x1 = self.x1_var.get()
        x3_sol = achar_x3_para_fy_zero(x1)
        if x3_sol is not None:
            self.x3_var.set(round(x3_sol, 2))
            self.atualizar()

    def resolver_item_b(self) -> None:
        x1 = self.x1_var.get()
        x3_base = achar_x3_para_fy_zero(x1)
        if x3_base is None:
            return

        x3_rot = achar_x3_para_rotacao(x1, 30.0, x3_base)
        if x3_rot is not None:
            self.x3_var.set(round(x3_rot, 2))
            self.atualizar()

    def atualizar(self) -> None:
        x1 = self.x1_var.get()
        x3 = self.x3_var.get()

        f = soma_forcas_sobre_particula_1(x1, x3)
        x3_a = achar_x3_para_fy_zero(x1)

        info = [
            f"x1 = {x1:6.2f} cm",
            f"x3 = {x3:6.2f} cm",
            "",
            f"Fx = {f.x:+.3e} N",
            f"Fy = {f.y:+.3e} N",
            f"|F|= {f.mod:.3e} N",
            f"ângulo = {f.ang_deg:+.2f}°",
        ]

        if x3_a is not None:
            f_a = soma_forcas_sobre_particula_1(x1, x3_a)
            info += [
                "",
                f"(a) x3 para Fy≈0: {x3_a:.2f} cm",
                f"    Fy nesse ponto: {f_a.y:+.2e} N",
            ]

            x3_b = achar_x3_para_rotacao(x1, 30.0, x3_a)
            if x3_b is not None:
                f_b = soma_forcas_sobre_particula_1(x1, x3_b)
                delta = (f_b.ang_deg - f_a.ang_deg + 180) % 360 - 180
                info += [
                    f"(b) x3 para +30°: {x3_b:.2f} cm",
                    f"    rotação obtida: {delta:+.2f}°",
                ]

        self.lbl_info.config(text="\n".join(info))
        self._desenhar_cena(x1, x3, f)

    def _desenhar_cena(self, x1: float, x3: float, forca: Vetor2D) -> None:
        self.canvas.delete("all")

        w = self.canvas.winfo_width() or 700
        h = self.canvas.winfo_height() or 600
        cx, cy = w // 2, h // 2
        escala = 16

        self.canvas.create_line(40, cy, w - 40, cy, fill="#666", width=2)
        self.canvas.create_line(cx, 40, cx, h - 40, fill="#666", width=2)
        self.canvas.create_text(w - 30, cy - 12, text="x", fill="#444")
        self.canvas.create_text(cx + 12, 24, text="y", fill="#444")

        particulas = [
            (x1, 0.0, "1", "#d9534f"),
            (0.0, -10.0, "2", "#337ab7"),
            (x3, 0.0, "3", "#5bc0de"),
            (0.0, +5.0, "4", "#337ab7"),
            (0.0, 0.0, "5(+)", "#5cb85c"),
        ]

        for xp, yp, nome, cor in particulas:
            px = cx + xp * escala
            py = cy - yp * escala
            r = 8
            self.canvas.create_oval(px - r, py - r, px + r, py + r, fill=cor, outline="")
            self.canvas.create_text(px + 14, py - 10, text=nome, fill="#222", font=("Arial", 9, "bold"))

        f_scale = 2e21
        ex = cx + x1 * escala
        ey = cy
        vx = forca.x * f_scale
        vy = -forca.y * f_scale
        self.canvas.create_line(ex, ey, ex + vx, ey + vy, arrow=tk.LAST, width=3, fill="#ff6600")
        self.canvas.create_text(ex + vx + 60, ey + vy, text="F resultante em 1", fill="#ff6600")

        self.canvas.create_text(
            12,
            12,
            anchor="nw",
            text="Unidades de posição em cm. Vetor de força está ampliado para visualização.",
            fill="#555",
            font=("Arial", 9),
        )


if __name__ == "__main__":
    App().mainloop()
