def genFibonacci(n):
   assert n >= 2
   sum=[0, 1]
   prev1=0
   prev2=1
   for i in range(2,n):
      sum.append(prev1+prev2)
      prev1=sum[-1]
      prev2=sum[-2]
   return sum

def genFib(n):
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    sum=genFib(n-1)[-1]+genFib(n-2)[-1]
    return genFib(n-1)+[sum]

def gen_fast(n, prev1, prev2, lim):
    if n>=lim:
        return prev1+prev2
    return gen_fast(n+1, prev1+prev2, prev1, lim)

def gen_fast_list(n, prev1, prev2, lim):
    if n>=lim-1:
        return [prev1+prev2]
    if n==0:
        return [0]+gen_fast_list(n+1, 0, 1, lim)
    return [prev1+prev2]+gen_fast_list(n+1, prev1+prev2, prev1, lim)


def genFib_recursive_weird(n, prev1, prev2, lim):
    if n==0 or n>lim:
        return 0
    if n==1:
        return 1
    soma=prev1+prev2
    
    return soma+genFib_recursive_weird(n+2, genFib_recursive_weird(n+1, soma, prev1, lim), soma, lim)

print(genFibonacci(29))
print(genFib(15))
print(gen_fast_list(0,0,0,29))
print(gen_fast(1,1,0,900))
#print(genFib_recursive_weird(2, 1, 0, 20))
