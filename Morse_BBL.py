def biblio(letra, caso):
    A = ['A', '.-']
    B = ['B', '-...']
    C = ['C', '-.-.']
    D = ['D', '-..']
    E = ['E', '.']
    F = ['F', '..-.']
    G = ['G', '--.']
    H = ['H', '....']
    I = ['I', '..']
    J = ['J', '.--']
    K = ['K', '-.-']
    L = ['L', '.-..']
    M = ['M', '--']
    N = ['N', '-.']
    O = ['O', '---']
    P = ['P', '.--.']
    Q = ['Q', '--.-']
    R = ['R', '.-.']
    S = ['S', '...']
    T = ['T', '-']
    U = ['U', '..-']
    V = ['V', '...-']
    W = ['W', '.--']
    X = ['X', '.--']
    Y = ['Y', '-.--']
    Z = ['Z', '--..']
    branco = [' ', ' ']
    afl = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, branco]
    index1 = 0
    if caso == 1:
        letra = letra.upper()
        while letra != afl[index1][0]:
            index1 += 1
        else:
            letra = afl[index1][1]
        return letra
    elif caso == 2:
        while letra != afl[index1][1]:
            index1 += 1
        else:
            letra = afl[index1][0]
        return letra
