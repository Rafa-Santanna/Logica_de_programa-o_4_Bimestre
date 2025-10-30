#Ler 8 elementos de uma matriz A do tipo vetor. Criar uma matriz B de
#mesmo tipo, observando a seguinte lei de formação: “Todo elemento de B
#deverá ser o quadrado do elemento de A correspondente”.

A=[]
B=[]

for i in range(5):
    num=int(input("Digite o valor da lista"))
    A.append(num)
for i in range(5):
    C=A[i]**2
    print(C)
