import os
os.system ("cls")

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

# Cálculo do total
total = quantidade * preco_unitario

# Determinação do desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Cálculo do total a pagar
total_a_pagar = total - desconto

# Exibição dos resultados
print(f"\nProduto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
