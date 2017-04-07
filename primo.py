n = int(input("Digite um número inteiro: "))

i = 1

while  i != 0:
    n2 = n % 2
    n3 = n % 3
    n5 = n % 5
    i = i - 1
if n2 and n3 and n5 != 0 or n == 2 or n == 3 or n == 5:
    print("primo")
else:
    print("não primo")
