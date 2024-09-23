#Solução de programa da semana...
DIA = input("Digite o dia da semana:")
match DIA:
    case "segunda":
        print("Vou para academia!")
    case "terça":
            print("Melhor não contar...")
    case "quarta":
        print("Vou a praia")
    case "quinta":
        print("Vou ao cinema")
    case "sexta":
        print("Vou beber todas!")
    case "sábado":
        print("Vou descansar ")
    case "domingo":
        print("Vou a  missa")
    case _:
            print("Não entendi")
            
                  
