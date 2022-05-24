# url = https://projecteuler.net/problem=6
def s_square_n(n):
  s = (n*(n+1))/2
  s = s*s
  return s
def s_n_square(n):
  s = n*((2*n)+1)*(n+1)/6 
  return s
def square_dif(n):
  s =  s_square_n(n) - s_n_square(n)
  return s
print(square_dif(100))
