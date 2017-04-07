n = int(input("Digite um número inteiro: "))

i = n
soma = 0

while i != 0:
    soma = soma + (n % 10)
    n = n // 10
    i = i // 10

print(soma)
