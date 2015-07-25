dialogo = open('dialogo.txt')
dialogo.seek(0)
for linha in dialogo:
    ator, fala = linha.split(':')
    print(ator, end='')
    print(' diz: ', end='')
    print(fala, end='')
dialogo.close()
