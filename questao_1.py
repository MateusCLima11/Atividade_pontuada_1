import os
os.system("cls")



A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))


soma = A + B


if soma < C:
    print("A + B é menor que C.")
else:
    print("A + B é maior ou igual a C.")
