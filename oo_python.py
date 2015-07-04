class Pessoa(object):
    #Declaraçao de atributo da classe
    nome = ""
    idade = 0

    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print("A pessoa esta andando...")

#Instanciamos o objeto
#p = Pessoa()
p = Pessoa("Francisco Andre")
#Definimos o valor do atributo nome
#p.nome = "Francisco André"
#Definimos o valor do atributo idade
p.idade = 34
#Faz a impressao dos valores dos atributos
print("Nome:", p.nome, "Idade:", p.idade)
p.andar()
