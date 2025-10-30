#Ler duas matrizes A e B do tipo vetor com 5 elementos cada. Criar uma
#matriz C, onde cada elemento de A é a subtração do elemento correspondente
#de A com B. Exibir a matriz C.
A=[]
B=[]
C=[]

for i in range(5):
    num=int(input("Digite o valor da lista"))
    A.append(num)
for i in range(5):
    num=int(input("Digite o valor da lista"))
    B.append(num)
for i in range(5):
    C.append(A[i]-B[i])
print(C)
    
