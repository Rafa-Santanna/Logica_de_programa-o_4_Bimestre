nota1= float(input ("Digite a primeira nota:"))
nota2= float(input ("Digite a segunda nota:"))
M= (nota1+nota2)/2
if M>=6:
    print("Aprovado", M)
else:
    E= float(input ("Digite a nota de exame:"))
    Nm=(E+M)/2
    if Nm>=5:
        print("Aprovado em exame")
    else:
        print("Reprovado")    