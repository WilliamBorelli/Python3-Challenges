import math

x1 = int(input("Digite o primeiro número: "))
y1 = int(input("Digite o segundo número: "))
x2 = int(input("Digite o terceiro número: "))
y2 = int(input("Digite o quarto número: "))

d = math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)

if d >= 10:
    print("longe")
else:
    print("perto")
