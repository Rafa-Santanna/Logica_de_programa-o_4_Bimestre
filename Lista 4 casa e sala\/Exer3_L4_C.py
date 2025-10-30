RAV, RAC= [],[]
for i in range (9):
    RAV.append(int(input("Digite o valor do rav")))
RAC.append(RAV)  

RAC[5]=RAV[9]
RAC[6]=RAV[8]
RAC[7]=RAV[6]
RAC[8]=RAV[5]
print(RAC, RAV)