class Pessoa(object):

    def __init__(self, nome, mae):
        self.nome = nome
        self.mae = mae
        print("Método construtor da super classe")

    def andar(self):
        print("Aprendendo a caminhar!")

    def chorar(self):
        print("Muleque chorando pq caiu!!!")
