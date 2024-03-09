def sumsq(lis):
    s=0
    for x in lis:
        s+=x**2
    return s

def sumsq_recursive(lis):
    s=0
    if len(lis)>0:
        s0=lis[0]**2
        s=s0+sumsq_recursive(lis[1:])
    return s

def sumsq_divide_and_conquer(lis):
    if len(lis)==1:
        return lis[0]**2

    meio=len(lis)//2
    cena=sumsq_divide_and_conquer(lis[0:meio])
    dor=sumsq_divide_and_conquer(lis[meio:])

    return cena+dor

lis = [29, 1, 1996]
print(sumsq(lis))
print(sumsq_recursive(lis))
print(sumsq_divide_and_conquer(lis))