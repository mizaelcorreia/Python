"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.
"""
        
N = int(input("Digite o valor de N: "))
div = 0
for i in range(1, N+1):
    primo = True

    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1

    if primo:
        print(i)

print("Fiz %i divisões"%div)

div = 0
for i in range(1, N+1):
    primo = True

    for j in range(2, i):
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i)

print("Fiz %i divisões"%div)


"""

***Solucao 1

N=7

div = 0

for(1,8)

primo = True

j = 2

while 2 < 1 (false) e primo (true) ***nao executa

print = 1

__________________________________________________

N=7

div = 0

for(2,8)

primo = True

j = 2

while j = 2 < i = 2 (false) e primo (true) ***nao executa


if primo(true)***executa
print = 2


___________________________________________________________


N=7

div = 0

for(3, 8)

primo = True

j = 2

while j=2 < i=3 (true) e primo (true) ***executa
div = 1
if 3 % 2 == O (False) ***nao executa

j = 2 + 1 = 3


while j = 3 < i = 3 (false) e primo (true) ***nao executa

if primo(true) ***executa
print = 3

______________________________________________________________


N = 7

for(4,8)

primo = true

j = 2

while j = 2 < i = 4 (true) e primo (true) ***executa
div = 1 + 1+ = 2
if 4 % 2 == 0 (True) ***executa
primo = Falso

while j = 3 < i = 4 (true) e primo (false) ***nao executa

if primo(false)***nao executa

__________________________________________________________________

N = 7

for(5, 8)

primo = True

j = 2

while j = 2 < i = 5 (true) e primo (true) ***executa

div = 2 + 1 = 3

if 5 % 2 == 0 (False) ***nao executa

j = 2 + 1 = 3



while j = 3 < i = 5 (true) e primo (true) ***executa

div = 3 + 1 = 4

if 5 % 3 == 0 (False) ***nao executa

j = 3 + 1 = 4


while j = 4 < i = 5 (true) e primo (true) ***executa

div = 4 + 1 = 5 

if 5 % 4 == 0 (False) ***nao executa

j = 4 + 1 = 5


while j = 5 < i = 5 (False) e primo (True) ***nao executa

if primo (True) ****executa

print = 5

______________________________________________________________

N = 7

for(6,8)

primo = True

j = 2

while j = 2 < i = 6 (True) e primo (True) ***executa
div = 5 + 1 = 6
if 6 % 2 == 0 (True) ***executa
primo = Falso


if primo(False)***nao executa

__________________________________________________________________


N = 7

for(7,8)

primo = True

j = 2

while j = 2 < i = 7 (True) e primo (True) ***executa
div = 6 + 1 = 7
if 7 % 2 == 0 (False) ***nao executa
j = 2 + 1 = 3


while j = 3 < i = 7 (True) e primo (True) ***executa
div = 7 + 1 = 8
if 7 % 3 == 0 (False) ***não executa
j = 3 + 1 = 4


while j = 4 < i = 7 (True) e primo (True) ***executa
div = 8 + 1 = 9
if 7 % 4 == 0 (False)***não executa
j = 4 + 1 = 5



while j = 5 < i = 7 (True) e primo (True) ***executa
div = 9 + 1 = 10
if 7 % 5 == 0 (False)***não executa
j = 5 + 1 = 6


while j = 6 < i = 7 (True) e primo (True) ***executa
div = 10 + 1 = 11
if 7 % 5 == 0 (False)***não executa
j = 6 + 1 = 7


while j = 7 < i = 7 (True) e primo (True) ***nao executa

if primo(True)***executa

print = 7
__________________________________________________________________


****sai do for

print= 11

___________________________________________________________________

***Solucao 2


N = int(input("Digite o valor de N: "))
div = 0


for i in range(1, N+1):
    primo = True

    for j in range(2, i):
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i)

print("Fiz %i divisões"%div)

______________________________________________________________________


N = 7
div = 0


for i in range(1, 7+1):
    primo = True

    for j in range(2, i):
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i)

print("Fiz %i divisões"%div)

______________________________________________________________________


N = 7
div = 0


for i in range(1, 8):
    primo = True

    for j in range(2, 1):****nao executa
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i) //print = 1

______________________________________________________________________


N = 7
div = 0


for i in range(2, 8):
    primo = True

    for j in range(2, 2):****nao executa
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i) //print = 2

______________________________________________________________________


N = 7
div = 0


for i in range(3, 8):
    primo = True

    for j in range(2, 3):****executa
        div += 1 			# div = 1
        if i % j == 0:***nao executa
            primo = False

    if primo:
        print(i) ####print = 3

______________________________________________________________________


N = 7
div = 0


for i in range(4, 8):
    primo = True

    for j in range(2, 4):****executa
        div = 1 + 1 = 2
        if 4 % 2 == 0: #True
            primo = False


	for j in range(3, 4):****executa
        div = 2 + 1 = 3
        if 4 % 3 == 0: #False***nao executa
            primo = False


	for j in range(4, 4):****nao executa
        div = 2 + 1 = 3
        if 4 % 3 == 0: #False***nao executa
            primo = False

    if primo: #False***nao executa
        print(i) 


______________________________________________________________________


N = 7
div = 0


for i in range(5, 8):
    primo = True

    for j in range(2, 5):****executa
        div = 3 + 1 = 4
        if 5 % 2 == 0: #False***nao executa
            primo = False


	for j in range(3, 5):****executa
        div = 4 + 1 = 5
        if 5 % 3 == 0: #False***nao executa
            primo = False


	for j in range(4, 5):****nao executa
        div = 5 + 1 = 6
        if 5 % 4 == 0: #False***nao executa
            primo = False

	for j in range(5, 5):****nao executa

	if primo #True***executa
	print(i)# Print = 5

______________________________________________________________________


N = 7
div = 0


for i in range(6, 8):
    primo = True

    for j in range(2, 6):****executa
        div = 6 + 1 = 7
        if 6 % 2 == 0: #True***executa
            primo = False



	for j in range(3, 6):****executa
        div = 7 + 1 = 8
        if 6 % 3 == 0: #True***executa
            primo = False

	for j in range(4, 6):****executa
        div = 8 + 1 = 9
        if 6 % 4 == 0: #False***nao executa
            primo = False

    for j in range(5, 6):****executa
        div = 9 + 1 = 10
        if 6 % 5 == 0: #False***nao executa
            primo = False
	
	for j in range(6, 6):****nao executa

	if primo:###False***nao executa
		print(i)#
	

______________________________________________________________________


N = 7
div = 0


for i in range(7, 8):
    primo = True

	for j in range(2, 7):****executa
        div = 10 + 1 = 11
        if 7 % 2 == 0: #False***nao executa
            primo = False
	   
	for j in range(3, 7):****executa
        div = 11 + 1 = 12
        if 7 % 3 == 0: #False***nao executa
            primo = False

    for j in range(4, 7):****executa
        div = 12 + 1 = 13
        if 7 % 4 == 0: #False***nao executa
            primo = False

    for j in range(5, 7):****executa
        div = 13 + 1 = 14
        if 7 % 5 == 0: #False***nao executa
            primo = False    

	for j in range(6, 7):****executa
        div = 14 + 1 = 15
        if 7 % 6 == 0: #False***nao executa
            primo = False


	for j in range(7, 7):****nao executa

    if primo: #True***nao executa
        print(i)###print = 7 

print = 15


		


"""