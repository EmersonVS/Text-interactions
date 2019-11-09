import Caixa_AB as CAB
import Inverter_V2 as IV2
import Morse_LGC as ML1
import Morse_LGC2 as ML2
param = -1
rec = 1
while rec != 0:
    while param not in (0,1,2,3,4):
        param = int(input("1 - Inverter \n"
                      "2 - Mongol \n"
                      "3 - Para Morse \n"
                      "4 - Para Alfabeto\n"
                      "0 - Para sair\n"
                      "Faça sua escolha! \n"))
    if param == 1:
        A = input("Digite a frase para ser invertida:\n")
        A = IV2.inverter(A)
    if param == 2:
        A = input("Digite a frase para ser mongolizada:\n4")
        A = CAB.mongol(A)
    if param == 3:
        A = input("Digite a frase para ser transformada em morse:\n")
        A = ML1.morse(A)
    if param == 4:
        A = input("Digite o código para ser decifrado:\n")
        A = ML2.morse2(A)
    if param == 0:
        break
    print(A)
    param = -1
print("Finalizado")