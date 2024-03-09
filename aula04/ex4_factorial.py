def factorial(n):
    assert isinstance(n, int), "n should be an int"
    assert n >= 0            , "n should not be negative"
    N=n
    if n==0:
        return 1
   
    for numero in range(1,n):
        n=n*numero
        
    print("Factorial(",N,") =",n)
    return n
    

def main():
    factorial(29)

main()