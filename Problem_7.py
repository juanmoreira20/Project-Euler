# url = https://projecteuler.net/problem=7
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True
def prime_list(n):
  v = []
  k = 1
  if n == 1:
    v.append(2)
  elif n == 2:
    v.append(2)
    v.append(3)
  else:
    v.append(2)
    v.append(3)
    while len(v)<n:
      a = 6*k-1
      b = 6*k+1
      t = v.copy()
      if is_prime(a):
        v.append(a)
      if is_prime(b):
        v.append(b)  
      k = k + 1
  return v
p = prime_list(10001)
print(p[-1])     
