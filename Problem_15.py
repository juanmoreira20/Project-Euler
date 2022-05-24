#Para encontrar a solução mais optimizada, devemos usar um artifício da combinatória
#Supondo 1 para quando ele vai para a direita e 0 quando ele vai para baixo, temos, no 2x2, que ele representa, independente de como ocorra o caminho
#Uma combinação relativa a uma palavra de 4 caracteres _ _ _ _, tal que, 2 precisam ser 1 e 2 precisam ser 0, logo, a solução combinatória é dada por 4escolhe2
#Para 20x20, temos a solução 40escolhe20, logo, o código se resume a:
import math
print(math.factorial(40)/(math.factorial(20)*math.factorial(20)))
