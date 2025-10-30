#Ler uma matriz A do tipo vetor com 6 elementos. Criar uma matriz B de
#mesmo tipo, sendo que cada elemento da matriz B seja o fatorial do elemento
#correspondente da matriz A. Exibir a matriz B.

import math
A=[]
B=[]
for i in range(5):
    num=int(input("Digite o valor da lista"))
    A.append(num)
    B.append(math.factorial(A[i]))  
    print(B)   



