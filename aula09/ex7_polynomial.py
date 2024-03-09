# COMPLETE a função abaixo.
# Veja os exemplos de utilização e resultados esperados.

# polynomial2(a,b,c) deve devolver uma função f tal que
# f(x) seja o polinómio de segundo grau ax²+bx+c.
def polynomial2(a, b, c):
    f = lambda x: a*x**2 + b*x +c
    return f


# DESAFIO EXTRA:
# Crie uma versão generalizada que cria polinómios de qualquer grau.
# (Não é tão fácil com expressões lambda.)

# polynomial(a), onde a=[a0, a1, ..., an], deve devolver uma função f tal que
# f(x) seja o polinómio a0*x**n + a1*x**(n-1) + ... + an.
""" def polynomial(coefs):                                  #1ª versão (sem lambda)
    #abcissas = [len(coefs[n:0:-1]) for n in coefs]
    def f(x):                       #função que vai ser retornada que aceita 1 argumento (como a polynomial2 também retorna uma função que aceita 1 parâmetro)
        y=0                             #resultado
        i=len(coefs)-1                  #potência
        for a in coefs:
            y += a*x**i
            i -= 1
        return y

    return f """


def polynomial(coefs):                              #2ª versão (com lambda, mas não funciona). Update: já funciona
    x = lambda a: sum(a)
    f = lambda y: x(coefs[len(coefs)-1-a]*y**a for a in range(len(coefs)-1, -1, -1))
    return f





def main():
    xx = [0, 1, 2, 3]   # Valores de x a testar

    print("\nTestes à função polynomial2:")
    p = polynomial2(1, 2, 3)    # creates p(x)=x²+2x+3
    print([p(x) for x in xx])   # [3, 6, 11, 18]

    q = polynomial2(2, 0, -2)   # creates q(x)=2x²-2
    print([q(x) for x in xx])   # [-2, 0, 6, 16]

    print("\nTestes à função polynomial:")
    r = polynomial([1, 2, 3])   # same as p(x)
    print([r(x) for x in xx])   # [3, 6, 11, 18]

    s = polynomial([1, -1, 0, 100])     # creates s(x)=x³-x²+100
    print([s(x) for x in xx])           # [100, 100, 104, 118]

if __name__ == "__main__":
    main()

