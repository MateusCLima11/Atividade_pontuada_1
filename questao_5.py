import os
os.system ("cls")

A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))

operacao = input("Digite a operação desejada (+,-,* ou /): ")

match operacao:
    case "+":
        soma = A + B
        print(f"Soma é igual a:{soma}")
    case "-":
        subtracao = A - B
        print(f"Subtração é igual a:{subtracao}")
    case "*":
        multiplicacao = A * B
        print(f"A multiplicação dos valores é igual a: {multiplicacao}")
    case "/":
        divisao = A / B
        if B != 0:
             print(f"A divisão é igual a: {divisao:.2f}")
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")        

