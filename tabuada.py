import os

os.system("cls || clear")

numeroEscolhido = 0
resposta = 'S'

while resposta == 'S':
    numeroEscolhido = int(input("\nDIGITE UM NÚMERO PARA GERAR A TABUADA: "))
    
    
    for i in range(1,11):
        print(f"{numeroEscolhido} x {i} = {numeroEscolhido * i}")

    resposta = input(f"\nDESEJA FAZER A TABUADA DE OUTRO NÚMERO? (S) P/ SIM OU (N) P/ NÃO \nRESPOSTA: ")
    resposta = resposta.upper()

