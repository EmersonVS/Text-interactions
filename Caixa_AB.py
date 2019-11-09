def mongol(mongol):
    palavra = ''
    index = 1
    for letra in mongol:
        if letra == ' ':
            index -= 1
        elif index % 2 != 0:
            letra = letra.upper()
        else:
            letra = letra.lower()
        palavra += letra
        index += 1
    return palavra
