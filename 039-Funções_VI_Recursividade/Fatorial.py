def fatorial(n):
    if n==1:
        return n
    return fatorial(n-1) * n


print(fatorial(5))

"""n = 5 --> ret = 5*fatorial(4)*fatorial(3)*fatorial(2)*fatorial(1) = 5*4*3*2*1
n = 4 --> fatorial(4) = 4*fatorial(3)*fatorial(2)*fatorial(1) = 4*3*2*1
n = 3 --> fatorial(3) = 3*fatorial(2)*fatoral(1) = 3*2*1
n = 2 --> fatorial(2) = fatorial(1)*2 = 1*2
n = 1 --> fatorial(1) = 1"""


print(fatorial(4))

"""
fatorial(5)

def fatorial(n)
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)

"""