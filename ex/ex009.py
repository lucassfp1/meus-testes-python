# EXERCICIO 25
print("-"*80)

name = input("Digite um nome: ")

if "Silva" in name:
    print("Tem Silva no nome!")
else:
    print("NAO tem Silva")

print("-"*80)

# EXERCICIO 26

frase = input("Digite uma frase: ").lower()

frase = frase.lower()
a = frase.count("a")
position = frase.find("a") + 1
rposition = frase.rfind("a") + 1

print(f"A letra 'a' aparece {a} vezes,\nela aparece pela primeira vez na posiçao {position}\ne aparece pela última em {rposition}")

print("-"*80)

# EXERCICIO 27

nome = input("Digite seu nome completo: ")

first = nome.split()[0]
last = nome.split()[2]

print(f"Ex: {nome}")
print(f"Primeiro: {first}")
print(f"Último: {last}")