import math

a= float(input ("Digite a primeira valor:"))
b= float(input ("Digite a segunda valor:"))
c= float(input ("Digite a terceira valor:"))
delta=float((b*b)-4*a*c)
if delta>0:
    x1=(-b+math.sqrt(delta))/ (2*a)
    x2=(-b-math.sqrt(delta))/ (2*a)
    print("O x1 e x2 é", x1, x2)