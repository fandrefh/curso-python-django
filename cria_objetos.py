from pessoa import Pessoa
from pessoa_bb import BB
from pessoa_vovo import Vovo

#Instanciando um objeto do tipo BB
bb1 = BB("João Gabriel", "Thaline André")
bb2 = BB("Novo BB", "Nova Mae")
#Imprime o BB criado...
print("Nome: " + bb1.nome)
print("Mãe: " + bb1.mae)
print("Nome: " + bb2.nome)
print("Mãe: " + bb2.mae)
#Método definido na super classe Pessoa
bb1.andar()
#Método definido na sub-classe BB
bb1.bicicleta()
#Médoto chorar da super classe
bb1.chorar()
print("--------------------------------------------")
#Instanciando um objeto do tipo Pessoa
p1 = Pessoa("João Miguel", "Emanuela Carvalho")
p2 = Pessoa("Nova Pessoa", "Nova Mae")
#Imprime a pessoa criada...
print("Nome: " + p1.nome)
print("Mãe: " + p1.mae)
print("Nome: " + p2.nome)
print("Mãe: " + p2.mae)
#Método definido na própria classe
p1.andar()
p1.chorar()
#Isso vai dá merda federal!!! :(
#p1.bicicleta() #Este método está definido na sub-classe, por isso não funciona. Somente métodos da super classe estão disponíveis nas sub-classes.
print("--------------------------------------------")
#Instanciando uma nova vovó...
vo = Vovo()
#Setando o nome da vovó
vo.nome = "Maria do Amparo"
#Imprime o nome da vovó
print(vo.nome)
#Chamada ao método da sub-classe Vovó
vo.idade(59)
#Acessando método sobrescrito da super classe
vo.andar()
