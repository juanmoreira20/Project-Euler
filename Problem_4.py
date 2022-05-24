# url = https://projecteuler.net/problem=4
for a in range (100,1000):
  for b in range(100,1000):
    n = a*b
    n_list = [int(x) for x in str(n)]
    n_reverse = n_list.copy()
    n_reverse.reverse()
    if n_list == n_reverse:
      v.append(n)      
print(max(v))
