from pessoa import Pessoa

class Vovo(Pessoa):

    nome = ""

    def __init__(self, nome=None, mae=None):
        super().__init__(nome, mae)

    #Sobrecarga do metodo da super classe
    def andar(self):
        print("Já sou bem grandinha, sei andar sozinha!")

    def idade(self, idade):
        self.idade = idade
        print("Eu tenho", idade, "anos.")
