def inverter(palavra):
    final = frase = ''
    pos = 0
    for letra in palavra:
        if letra == ' ':
            pos += 1
            letra = ''
            if pos == 1:
                frase = final
            else:
                frase = frase + ' ' + final
            final = ''
        final = letra + final
    frase = frase + ' ' + final
    return frase
