v = []
i = 1
a = 0
while i < 1000:
  if i%3 == 0 or i%5 == 0:
    a = a + i
    i = i+1
  else:
    i = i+1
print(a)      
