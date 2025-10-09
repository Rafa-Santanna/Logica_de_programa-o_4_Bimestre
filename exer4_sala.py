a= float(input ("Digite a primeira valor:"))
b= float(input ("Digite a segunda valor:"))
c= float(input ("Digite a terceira valor:"))
if a<b+c or b<a+c or c<a+b:
    if a==b or b==c or c==a:
        print("Isoceles")
    elif a==b==c:    
        print("Equilátero")
    else:
        print("Escaleno")  
else: 
        print("Não é triangulo")          

