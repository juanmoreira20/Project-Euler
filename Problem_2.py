# url = https://projecteuler.net/problem=2
def fibonacci(i, a = 1, b = 1, c = 0):
  sum = 0
  while c < i:
    c = a + b
    if c < i:
      b = a
      a = c
      if c%2 == 0:
        sum = sum + c
      else:
        pass  
    else:
      pass
  print(sum)     
fibonacci(4*(10**6)) 
