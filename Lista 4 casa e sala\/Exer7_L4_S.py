#Ler 10 elementos de uma matriz A tipo vetor e criar uma matriz de mesma
#dimensão com os mesmos elementos de A, sendo que esses deverão estar
#invertidos, ou seja, o 1º elemento de A passa a ser o último de B, o 2º elemento
#de A passa a ser o penúltimo e A e assim por diante.

A=[]
for i in range(10):
    A.append(int(input("Digite o valor")))
A.reverse()    
print(A)

