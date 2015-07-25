dialogo = open('dialogo.txt')
dialogo.seek(0)
for linha in dialogo:
    if not linha.find(':') == -1:
        ator, fala = linha.split(':', 1)
        print(ator, end='')
        print(' diz: ', end='')
        print(fala, end='')
dialogo.close()
