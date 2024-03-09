# Devolve o número de linhas da matriz M.
def matrows(M):
   return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
   return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
   #M = n * [0]   # MODIFY THIS...
   M=[]
   for i in range(m):
      M.append(n*[0]) 
   return M

def matzerosTEST(m, n):
   M = matzeros(m, n)
   M[0][1] = 1   # should change just 1 element!
   return M

# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
   assert matcols(A) == matrows(B)
   #C = matzeros(matrows(A), 0)
   #i=0
   #for linha in A:
   #   for j in range(matrows(A)):
   #      coluna = [x[j] for x in B]
   #      C[i].append(sum([linha[k]*coluna[k] for k in range(len(linha))]))
   #   i+=1
   #return C
   
   C = matzeros(matrows(A), matcols(B))
   for i in range(matrows(A)):   #para cada linha de A, m
      for j in range(matcols(B)):   #para cada coluna de B, p: somar a multiplicação dos n elementos da linha de A pelos n elementos de B
         C[i][j] = sum(A[i][x]*B[x][j] for x in range(matcols(A)))   #multiplicação de matrizes só é possível para matrizes A*B=C: m,n * n,p = m,p (matcols(A) = matrows(B) =  n)
   return C

def matmultTEST(A, B):
   C = matmult(A, B)
   return A, B, C


pass	
print(matcols([[1, 2, 3], [4, 5, 6]])) #3

pass	
matcols([[1, 2, 3, 4]]) #4

pass	
matcols([[1], [2], [3]]) #1

pass	
matzeros(3, 2) #[[0, 0], [0, 0], [0, 0]]

pass	
matzeros(2, 5) #[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pass	
matzeros(1, 1) #[[0]]
pass	
matzerosTEST(3, 4) #[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

pass	
matmult([[1, 0], [2, 3]], [[4, 5], [0,6]]) #[[4, 5], [8, 28]]

pass	
matmult([[4, 5], [0,6]], [[1, 0], [2, 3]]) #[[14, 15], [12, 18]]
pass	
matmult([[1, 2, 3], [4, 5, 6]],  [[7, 8], [9, 0], [1, 2]]) #[[28, 14], [79, 44]]
pass	
print(matmult([[7, 8], [9, 0], [1, 2]], [[1, 2, 3], [4, 5, 6]])) #[[39, 54, 69], [9, 18, 27], [9, 12, 15]]
pass	
matmultTEST([[1, 0], [2, 3]], [[4, 5], [0,6]]) #([[1, 0], [2, 3]], [[4, 5], [0, 6]], [[4, 5], [8, 28]])
