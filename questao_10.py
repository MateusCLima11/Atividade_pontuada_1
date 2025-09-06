import os
os.system ("cls")


preco_alcool = 3.79
preco_gasolina = 6.59


litros = float(input("Digite a quantidade de litros desejada: "))
tipo = input("Digite o tipo de combustível desejado (A para álcool, G para gasolina): ").strip().upper()


if tipo == "A":
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
    preco_bruto = litros * preco_alcool
elif tipo == "G":
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
    preco_bruto = litros * preco_gasolina
else:
    print("Tipo de combustível inválido.")
    desconto = 0
    preco_bruto = 0


valor_desconto = preco_bruto * desconto
valor_final = preco_bruto - valor_desconto


if preco_bruto > 0:
    print(f"Valor bruto: R$ {preco_bruto:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_final:.2f}")
