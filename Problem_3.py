# url = https://projecteuler.net/problem=3
def max_factor(n):
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
    print(fatores[-1])

max_factor(600851475143)
