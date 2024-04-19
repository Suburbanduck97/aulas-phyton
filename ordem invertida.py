import os
os.system("cls || clear")

numeros = []
numero = 1

for i in range(6):
   while(numero % 2 != 0 or numero < 0):
        numero = int(input(f"Digite o {i+1}º número positivo e par: "))
        numeros.append(numero)    

for i in range(len(numeros, -7,1)):
    print(f"{i-1}º número: {numeros[i]}")
    
