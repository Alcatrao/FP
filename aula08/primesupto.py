
def primesUpTo(n):
    conjunto = {n for n in range(2,n+1)}
    p=2
    usado = [p]
    while True:
        eratostenes = {n for n in conjunto if n%p==0 and n >= p**2}
        #print(p, eratostenes)
        if p >= n//2:
            return conjunto
        conjunto.difference_update(eratostenes)
        usado.append(p)
        p = min([n for n in conjunto if n not in usado])

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

