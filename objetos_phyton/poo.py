import os
class Vendedor:
    def __init__(self,nome):
        self.nome = nome
        self.vendas = 0

    def Vendeu(self,vendas):
        self.vendas = vendas

    def bateu_meta(self,meta):
        if self.vendas > meta:
            print(self.nome, "Bateu a meta!")
        else:
            print(self.nome, "Não bateu a meta!")

os.system("cls || clear")

vendedor1 = Vendedor("Lira")
vendedor1.Vendeu(1000)
vendedor1.bateu_meta(600)
