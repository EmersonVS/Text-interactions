import Morse_BBL as MS
def morse(A):
    caso = 1
    final = ''
    for letra in A:
        if letra == ' ':
            letra = ''
            final += letra
        else:
            morse = MS.biblio(letra, caso) + ' '
            final = final + morse
    return final