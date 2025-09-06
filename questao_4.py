import os
os.system ("cls")

# Leitura das quantidades
kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

# Determinação do preço por Kg
preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

# Cálculo dos valores
valor_morango = kg_morango * preco_morango
valor_maca = kg_maca * preco_maca
valor_total = valor_morango + valor_maca
peso_total = kg_morango + kg_maca

# Verificação de desconto
desconto_aplicado = False
if peso_total > 10 or valor_total > 15.00:
    valor_sem_desconto = valor_total
    valor_total *= 0.90  # Aplica 10% de desconto
    desconto_aplicado = True

# Exibição dos resultados
print("\n--- RESUMO DA COMPRA ---")
print(f"Morango: {kg_morango:.2f} Kg x R$ {preco_morango:.2f} = R$ {valor_morango:.2f}")
print(f"Maçã:    {kg_maca:.2f} Kg x R$ {preco_maca:.2f} = R$ {valor_maca:.2f}")

if desconto_aplicado:
    print(f"\nValor sem desconto: R$ {valor_sem_desconto:.2f}")
    print("Desconto aplicado: 10%")
else:
    print("\nDesconto não aplicado.")

print(f"\nValor final a pagar: R$ {valor_total:.2f}")