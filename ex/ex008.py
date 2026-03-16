# EXERCICIO 22

name = input("Qual o seu nome completo? ")
total = name.split()

print(f"O seu nome em letras maisculas fica: {name.upper()}")
print("-"*60)
print(f"O seu nome em letras minusculas fica: {name.lower()}")
print("-"*60)
print(f"A quantidade de letras em seu nome é: {len(name.replace(" ",""))}")
print("-"*60)
print(f"A quantidade do primeiro nome é: {len(total[0])}")
print("-"*80)

# EXERCICIO 23

num = input("Digite um numero entre 0 e 9999: ")
U = num[3]
D = num[2]
C = num[1]
M = num[0]

print(f"O seu número tem:\nUnidade: {U}\nDezena: {D}\nCentena: {C}\nMilhar: {M}")
print("-"*80)

#num = int(input("Digite um numero entre 0 e 9999: "))
#
#U = num // 1 % 10
#D = num // 10 % 10
#C = num // 100 % 10
#M = num // 1000 % 10

#print(f"O seu número tem:\nUnidade: {U}\nDezena: {D}\nCentena: {C}\nMilhar: {M}")

# EXERCICIO 24

name2 = input("Diga o nome de uma cidade: ")

if "Santo" in name2:
    print("A sua cidade tem Santo no nome!")
else:
    print("A sua cidade nao tem Santo no nome!")
