# url = https://projecteuler.net/problem=5
def factors(n):
    fatores = []
    for i in range(1, int((n**(1/2)))+1):
        if n%i == 0:
            prime = True
            for j in range(2, int((i**(1/2)+1))):
                if i%j == 0:
                    prime = False
                    break
                prime = True
            if prime:
                fatores.append(i)
    if len(fatores) == 1:
      fatores.append(n)
    return fatores
def divisible_until(n):  
  a = []
  for i in range(n,0,-1):
    v = factors(i)
    for j in range(len(v)):
      a.append(v[j])
  a = list(set(a))
  b = 1
  for k in range (len(a)):
    b = b*a[k]
  w = 2
  while w < n**(1/2):
    b = b*w
    w = w+1
  return b  
print (divisible_until(20))  
