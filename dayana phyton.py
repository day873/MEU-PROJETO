# Programa de tv/ série ...
print(input("Digite um filme ou série de sua preferência:"))
print("Qual nota vc dá para este programa de 1 a 5?")
print("1")
print("2")
print("3")
print("4")
print("5")
NOTA = int(input())

match NOTA:
    case 1:
        print("Péssimo!")
        PORQUE = input("Porque seu programa recebeu esta nota?")
    case 2:
        print("Ruim")
        PORQUE = input("Porque seu programa recebeu esta nota?")
    case 3:
        print("Razoável")
    case 4:
        print("BOM")
    case 5:
        print("Excelente")
    case _:
        print("ALERTA")
        
