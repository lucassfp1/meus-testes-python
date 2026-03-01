#desafio 9

num = int(input("Digite um número! "))
m = num*1
m1= num*2 
m2 = num*3 
m3 = num*4 
m4 = num*5 
m5 = num*6 
m6 = num*7 
m7 = num*8 
m8 = num*9 
m9 = num*10
print(f"A tabuada do seu número é \n{num} x 1 = {m} \n{num} x 2 = {m1} \n{num} x 3 = {m2} \n{num} x 4 = {m3} \n{num} x 5 = {m4} \n{num} x 6 = {m5} \n{num} x 7 = {m6} \n{num} x 8 = {m7} \n{num} x 9 = {m8} \n{num} x 10 = {m9}.")

#desafio 10

real = int(input("Quantos reais você tem? "))
dolar = real/3.27
print(f"Com {real} reais, você pode comprar {dolar:.1f} dólares!")

#desafio 11

alt = int(input("Quantos metros mede a altura da parede? "))
lar = int(input("E quanto mede a largura? "))
met2 = alt*lar
l = met2/2
print(f"Uma parede com {met2} m2, precisa de {l} litros de tinta para ser completa!")

#desafio 12

valor = int(input("Qual o valor do produto desejado? "))
desc = valor*(5/100)
final = valor-desc
print(f"Na liquidação o valor de R${valor:.2f}, terá um desconto de 5% aplicado. Ficando apenas R${final:.2f}!")

#desafio 13

sal = int(input("Qual o seu salário mensal? "))
ajus = sal*(15/100)
fin = sal + ajus
print(f"O seu reajuste salarial de 15% ficará R${fin:.2f}!")

