import os
os.system ("cls")


nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()


if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input("Digite o tempo de casada (em anos): ")
else:
    tempo_casada = "Não se aplica"


print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
print(f"Tempo de Casada: {tempo_casada}")
