def intersects(a1, b1, a2, b2):
    if b1>a2:
        return True
    return False

def main():

    a1=0
    b1=29
    a2=29
    b2=1996

    print(intersects(a1,b1,a2,b2))

main()