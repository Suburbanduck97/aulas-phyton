import os
import time
os.system("cls || clear")

maiorIdade = 0
menorIdade = 999
opcoes = 1
mediaSalario = 0.0
somaSalario = 0.0
mulheresAcima5K = 0
contador = 0

while(opcoes == 1 or opcoes == 2):
    os.system("cls || clear")
    print("=== SELECIONE A OPÇÃO ===\n")
    print("1 - Adicionar usuário \n2 - Exibir resultado \n3 - Sair")
    opcoes = int(input("Digite a opção desejada: "))
    os.system("cls || clear")

    if(opcoes == 1):
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo (F) para feminino ou (M) para masculino: ")
        sexo = sexo.upper()
        salario = float(input("Digite seu salário: R$"))
        
        contador+=1

        somaSalario += salario
        
        if(idade > maiorIdade):
            maiorIdade = idade

        if(idade < menorIdade):
            menorIdade = idade    

        if(sexo == 'F' and salario >= 500):
            mulheresAcima5K+=1
    elif(opcoes == 2):
        try:
            mediaSalario = somaSalario / contador
        except:
            print("\nInsira dados na página anterior...")

        print("=== EXIBINDO RESULTADOS ===")
        print(f"Média salarial: R${mediaSalario: .2f}")
        print(f"Maior Idade: {maiorIdade}")
        print(f"Menor Idade: {menorIdade}")
        print(f"Quantidade de mulheres que recebem acima de 5mil: {mulheresAcima5K}")
        time.sleep(5)
    
    elif(opcoes == 3):
        break

    
