import os
import time
from dataclasses import dataclass

def nomeDoSoftware():
    os.system("cls || clear")
    print("==== Controle de funcionário ====\n")


def salvandoDadosDoObjeto(listaDeDadosDosFuncionarios):
    tituloDoArquivo = 'Funcionarios.txt'
    with open (tituloDoArquivo, 'w', encoding= 'UTF-8') as arquivo:
        for dadosDoFuncionario in listaDeDadosDosFuncionarios:
            arquivo.write(F"{dadosDoFuncionario.nomeCompleto},{dadosDoFuncionario.cpf},{dadosDoFuncionario.cargo},{dadosDoFuncionario.salario}\n")
            print("Dados salvos!")
            time.sleep(3)

def lendoDadosDoFuncionario(listaDeDadosDosFuncionarios):
    tituloDoArquivo = 'Funcionarios.txt'
    armazenandoDadosDoFuncionario = []

    with open(tituloDoArquivo, 'r', encoding= 'UTF-8') as arquivo:
        for linha in arquivo:
            nomeCompleto, cpf, cargo, salario = linha.strip().split(',')
            armazenandoDadosDoFuncionario.append(Funcionario(nomeCompleto= nomeCompleto, cpf= cpf, cargo= cargo, salario= float(salario)))

        print("Funcionários da empresa: \n")
        for i in armazenandoDadosDoFuncionario:
            print(f"Nome do funcionário: {i.nomeCompleto}")
            print(f"CPF: {i.cpf}")
            print(f"Cargo: {i.cargo}")
            print(f"Salário: R${i.salario: .2f}")
            print()
            time.sleep(6)


def menuDeOpcoes():
    print("1. Registrar funcionário")
    print("2. Ver funcionários registrados")
    print("3. Encerrar programa")

@dataclass
class Funcionario:
    nomeCompleto : str
    cpf : str
    cargo : str
    salario : float

funcionariosDaEmpresa = []

while True:
    nomeDoSoftware()
    menuDeOpcoes()
    opcoesDoMenu = int(input("Digite a opção que deseja: "))

    if opcoesDoMenu == 1:
        nomeDoSoftware()
        dadosDoFuncionario = Funcionario(
            nomeCompleto = input("Digite o nome do funcionário: ").lower().title(),
            cpf = input("Digite o CPF do funcionário: "),
            cargo = input("Digite o cargo do funcionário: ").lower().title(),
            salario = float(input("Digite o salário do funcionário: R$"))
        )
        funcionariosDaEmpresa.append(dadosDoFuncionario)
        print()

        salvandoDadosDoObjeto(funcionariosDaEmpresa)
    elif opcoesDoMenu == 2:
        nomeDoSoftware()
        lendoDadosDoFuncionario(funcionariosDaEmpresa)
    elif opcoesDoMenu == 3:
        print("Encerrando programa...")
        nomeDoSoftware()
        time.sleep(3)
        break
