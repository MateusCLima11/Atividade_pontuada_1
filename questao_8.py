import os
os.system ("cls")


cor = input("Digite a cor do CD (Verde, Azul, Amarelo ou Vermelho): ").strip().lower()


match cor:
    case "verde":
        print("Preço: R$ 10,00")
    case "azul":
        print("Preço: R$ 20,00")
    case "amarelo":
        print("Preço: R$ 30,00")
    case "vermelho":
        print("Preço: R$ 40,00")
    case _:
        print("Cor inválida. Por favor, digite uma cor válida.")
