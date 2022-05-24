def Collatz(n):
  if n%2 == 0:
    return n/2
  else:
    return 3*n+1
def chain(n):
  aux = 1
  while n != 1:
    n = Collatz(n)
    aux = aux +1
  return aux  
v = []
for i in range(2,10**(6)):
  k = chain(i)
  v.append(k)
a = v.index(max(v))
print(a+2)   
