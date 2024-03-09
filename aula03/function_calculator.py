def p(x):
    y = x**2 + 2*x + 3
    return y

def main():
    print(p(0))
    print(p(1))
    print(p(2))
    print(p(p(1)))

main()