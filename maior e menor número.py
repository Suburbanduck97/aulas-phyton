import os

os.system("cls || clear")

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º Valor: "))
    numeros.append(numero)

    maiorNumero = max(numeros)
    menorNumero = min(numeros)

os.system("cls || clear ")
for i in range(len(numeros)):
    print(f"{i+1}º Número Inserido: {numeros[i]}")

print(f"\nMaior número Digitado: {maiorNumero}")
print(f"Menor Número Digtado: {menorNumero}")
