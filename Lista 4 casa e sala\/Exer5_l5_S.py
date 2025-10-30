# Ler duas matrizes do tipo vetor A com 20 elementos e B com 30 elementos.
#Criar uma matriz C, sendo essa a junção das duas outras matrizes. Assim, C
#deverá ter a capacidade de armazenar 50 elementos. 

A=[]
B=[]
C=[]

for i in range(5):
    num=int(input("Digite o valor da lista"))
    A.append(num)
    num=int(input("Digite o valor da lista"))
    B.append(num)

C=A+B
print(C) 