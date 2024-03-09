#nº seqs. binárias sem 3 0s consecutivos
def binary_seq(n):
    if n<3:
        return 0
    if n==3:
        return 1
    return 2*binary_seq(n-1)+2**(n-4)-binary_seq(n-4)

def binary_seq_solution(n):
    if n<3:
        return 0
    if n==3:
        return 1
    return binary_seq_solution(n-1)+binary_seq_solution(n-2)+binary_seq_solution(n-3)+2**(n-3) #sol. oficial

print(binary_seq(9))
print(binary_seq_solution(9))

#nº de seq.s binárias sem 0s consecutivos
def nin(n):
    if n<1:
        return 0
    if n==1:
        return 2
    if n==2:
        return 3
    return nin(n-1)+nin(n-2) #sol. oficial

def bin(n):
    if n<1:
        return 1
    if n==1:
        return 2
    if n==2:
        return 3
    
    return 2*bin(n-2)+bin(n-3)

print(nin(16))
print(bin(16))


#nº seqs binárias sem 2 0s consecutivos (igual ao caso acima)
''' dor mau
'''
def bi(n):
    if n<1:
        return 0
    if n==1:
        return 2
    if n==2:
        return 3
    return bi(n-1)+bi(n-2)          #se acabar em 1, podemos dar-lhe append no final (o mesmo raciocínio pode ser feito para o início) de todas as combinações válidas de tamanho n-1. Se acabar em 0, o penúltimo dígito tem de ser 1, e o resto é igual a todas as combinações válidas de tamanho n-2.

def bi_dor(n):
    if n<1:
        return 0
    if n==1:
        return 2
    if n==2:
        return 3
    if n==3:
        return 5
    return 2*bi_dor(n-2)+bi_dor(n-3)    #se o penúltimo dígito (n-1) da seq de tamanho n for 1, então o último (n) pode ser 0 ou 1 (2*bi_dor(n-2), em que o 2* representa as 2 escolhas para o último dígito, e o bi_dor(n-2) representa todas as combinações válidas com tamanho n-2, visto que o penúltimo e último dígito são fixos).
                                        #Se for 0, o próximo (n) só pode ser 1, mas o antepenúltimo (n-2) também tem que ser 1, para que não hajam 0s consecutivos (bi_dor(n-3)).

print(bi(16))
print(bi_dor(16))



