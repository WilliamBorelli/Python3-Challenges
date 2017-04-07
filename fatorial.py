n = int(input("Digite o valor de n: "))

i = n
fatorial = 1

while i != 0:
    i = i - 1
    fatorial = fatorial * n
    n = n - 1

print(fatorial)
