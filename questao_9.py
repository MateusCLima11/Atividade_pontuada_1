import os
os.system ("cls")


renda_mensal = float(input("Digite sua renda mensal: R$ "))

valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: R$ "))

num_prestacoes = int(input("Digite o número de prestações desejadas: "))


valor_prestacao = valor_emprestimo / num_prestacoes


limite_emprestimo = renda_mensal * 10

limite_prestacao = renda_mensal * 0.3


if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")
    if valor_emprestimo > limite_emprestimo:
        print(f"O valor do empréstimo excede o limite permitido de R$ {limite_emprestimo:.2f}.")
    if valor_prestacao > limite_prestacao:
        print(f"O valor da prestação excede 30% da renda mensal (R$ {limite_prestacao:.2f}).")