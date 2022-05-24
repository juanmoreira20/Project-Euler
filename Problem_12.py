import time

start_time = time.time()
def triangle(n):
  s = n*(n+1)/2
  return s
def divisores(n):
    aux = 2
    for i in range(2, ((int(n**(1/2))) + 1)):
        if n % i == 0:
            aux = aux +1  
            outro_divisor = n // i
            if outro_divisor != i: 
                aux = aux +1 
    return aux 
k = 1
n = 1
while k < 500:
  s = triangle(n)
  k = divisores(s)
  n = n +1
print(triangle(n-1))

end_time = time.time()

total_time = end_time - start_time

print (total_time) 
