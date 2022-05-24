# url = https://projecteuler.net/problem=10
#solution 1:
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
def prime_list(n,a = 1, b = 1):
  k = 1
  t = 5
  while a<n and b < n:
    a = 6*k-1
    b = 6*k+1
    if is_prime(a):
      if a > n:
        break
      else:
        t = t+a  
      if is_prime(b):
        if b > n:
          break
      else:
        t = t+b   
    k = k + 1
  return t
p = prime_list(2000001)
print(p) 

#solution 2
