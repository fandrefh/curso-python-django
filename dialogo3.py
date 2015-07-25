dialogo = open('dialogo.txt')
dialogo.seek(0)
for linha in dialogo:
    ator, fala = linha.split(':', 1)
    print(ator, end='')
    print(' diz: ', end='')
    print(fala, end='')
dialogo.close()
