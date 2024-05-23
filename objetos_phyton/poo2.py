import os
from dataclasses import dataclass

os.system("cls || clear")

# Grava dados do arquivo
def salvar(lista):
    nome_arquivo = 'aluno.txt'
    with open (nome_arquivo, 'w') as arquivo:
        for aluno in lista:
            arquivo.write(f"{aluno.nome},{aluno.idade}\n")
    print(f"Dados gravados com sucesso.")

# Ler os dados no arquivo
def ler_dados_alunos(lista):
    arquivo_origem = 'aluno.txt'
    listaAlunos = []

    with open(arquivo_origem, 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            listaAlunos.append(Aluno(nome= nome, idade= int(idade)))

    print("\nExibindo dados.")
    for i in listaAlunos:
        print(f"Nome: {i.nome}")
        print(f"Idade: {i.idade}")
        print()


@dataclass
class Aluno:
    nome : str
    idade : int

QUANTIDADE_ALUNOS = 2

alunos = []

print("\nSolicitando dados ao usuário.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)
    print()

salvar(alunos)
ler_dados_alunos(alunos)
