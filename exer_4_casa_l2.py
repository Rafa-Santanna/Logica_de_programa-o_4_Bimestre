a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a>=b or a>=c:
    m=a
if b>=a or b>=c:
    m=b
if c>=b or c>=a:
    m=c
print("O numéro maior é", m)
if a<=b or a<=c:
    maa=a
if b<=a or b<=c:
    maa=b
if c<=b or c<=a:
    maa=c
print("O numéro menor é", maa)

if a != m and a != maa:
    meio = a
elif b != m and b != maa:
    meio = b
else:
    meio = c    
print("O numero do meio é", meio)

