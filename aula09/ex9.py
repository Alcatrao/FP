def integrate(f, a, b, n):                          #método da regra dos trapézios (para calcular o integral duma função usando a soma de n trapézios com altura (abcissas, contraintuitivamente à primeira vista) igual e bases menor e maior iguais ao valor da função no primeiro e último pontos da altura), aprendida em Métodos Numéricos e Estatísticos
   """The integral of f(x) for x between a and b.
   Aproximated using the trapezoidal rule with n uniform subintervals."""
   assert n >= 1
   sum=0
   #base = abs(b-a)/n
   for i in range(n+1):
      xi = a + (b-a)*(i/n)
      sum += ((b-a)/(2*n)) * 2*f(xi)
   sum -= ((b-a)/(2*n)) * f(a)
   sum -= ((b-a)/(2*n)) * f(b)
   return sum

def example(n): #calcular a aproximação da derivada da função (x-2)/(x+3) entre 0 e 1 através da regra dos trapézios (com n pontos)
   a = integrate(lambda x: (x-2)/(x+3), 0, 1, n)
   return a

print(integrate(lambda x: x**2, 0, 1, 100))
print(integrate(lambda x: x**2, 0, 1, 1000))
print(integrate(lambda x: x**3, 0, 1, 100))
print(example(100))
print(example(1000))