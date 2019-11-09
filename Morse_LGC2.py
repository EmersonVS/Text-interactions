import Morse_BBL as MOB
def morse2(A):
    final = ""
    lista = []
    index = 0
    caso = 2
    for letra in A:
        if letra != ' ':
            final += letra
        else:
            lista.append(final)
            final = ''
    lista.append(final)
    final = ''
    for unidade in lista:
        if unidade == '':
            lista.remove(unidade)
    while index < len(lista):
        final += MOB.biblio(lista[index], caso)
        index += 1
    return final