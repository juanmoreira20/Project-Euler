# url = https://projecteuler.net/problem=2
v = []
for i in range(1,1000):
  b = i
  for j in range(1,1000):
    c = j
    a = (b+c)*(b-c)
    if a > 0:
      s = a**(1/2)
      if s == int(s):
        v.append([int(s),b,c])
for i in range(len(v)):
  t = 0
  for j in range(3):
    t = t + v[i][j]
  if t == 1000:
    v.append(i)
mul = 1
for i in range(3):
  mul = mul *v[v[-1]][i] 
print(mul)
