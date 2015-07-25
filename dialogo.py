dialogo = open('dialogo.txt')
dialogo.seek(0)
for linha in dialogo:
    print(linha, end='')
dialogo.close()
