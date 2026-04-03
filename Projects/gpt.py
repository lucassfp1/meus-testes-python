# 1


let = str(input("Digite um nome: ").strip().lower())

if let[0] == "a":
    print("Esse nome começa com a letra A!")
else:
    print("Esse nome nao começa com a letra A!")

print("-="*30)


# 2


frase = input("Digite uma frase: ").lower()

print(f"A sua frase teve {frase.count('e')} letras E!")

print("-="*30)


# 3


num = int(input("Digite um numero inteiro: "))

if num % 5 == 0:
    print("O seu numero é multiplo de 5!")
else:
    print("O seu numero nao é multiplo de 5!")


# 4


frase = input("Digite um nome de uma cidade: ").lower().strip()

if frase.endswith("sul"):
    print("Essa cidade tem sul no nome!")
else:
    print("Essa cidade nao tem sul no nome!")


# 5


a = int(input("Digite um numero: "))    
b = int(input("Digite outro numero: "))  
c = int(input("Digite outro numero: "))

maior = a

if b > c and b > a:
   maior = b
if c > b and c > a:
   maior = c

print(f"Entre {a}, {b} e {c} o maior é {maior}!")


# 6 


name = input("Digite seu nome completo: ").split()

print(f"O seu nome completo tem um total de {len(name)} nomes!")


#7


udc = int(input("Digite um numero entre 0 e 999: "))

u = udc // 1 % 10
d = udc // 10 % 10
c =  udc // 100 % 10

print(f"O numero {udc}, tem {u} unidades, {d} dezenas, {c} centenas!")


# 8


python = input("Digite uma frase: ").lower()
if "python" in python:
    print("A sua frase tem python!")
else:
    print("A sua frase nao tem python!")


# 9 

salario = float(input("Digite o seu salario: "))

if salario > 2000:
    print("O seu salario é maior que 2000 reais!")
elif salario == 2000:
    print("O seu salario é de 2000 reais!")
else:
    print("O seu salario é menor que 2000 reais!") 


# 10

nameFull = input("Digite seu nome inteiro: ").split()

if len(nameFull[0]) == len(nameFull[-1]):
    print("O seu primeiro e ultimo nome tem o mesmo tamanho!")
else:
    print("O seu primeiro e ultimo nome nao tem o mesmo tamanho!")

