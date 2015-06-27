from random import randint
print("Bem vindo!!!")
# print(numero_sorteado)
novo_jogo = True
while novo_jogo != False:
        numero_sorteado = randint(1,100)
        contador = 1
	while True:
                
		chute = int(input("Chute um número: "))
		if chute == numero_sorteado:
			print("Parabéns, você é foda.")
			break
		else:
			print("Alto" if chute > numero_sorteado else "Baixo")
		contador += 1
	print("Fim de jogo!!!")
	print("Número sorteado: " + str(numero_sorteado))
	print("Número chutado: " + str(chute))
	print("Número de tentativas: " + str(contador))
	novo_jogo = int(input("Jogar novamente? 1 - Sim ou 0 - Não: "))
