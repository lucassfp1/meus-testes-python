# EXERCICIO 32

age = int(input("Digite um ano: "))

if age % 400 == 0:
    print("Bisexto!")
elif age % 100 == 0:
    print("Nao é bissexto")

elif age % 4 == 0:
    print("Bissexto")

else:
    print("Nao é bissexto")

print("-"*50)

# EXERCICIO 33

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
c = int(input("Terceiro numero: "))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O maior é {maior} e o menor é o {menor}!")    
