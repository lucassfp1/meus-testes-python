# EXERCICIO 30

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print('É Par!')
else:
    print("É impar!") 
print("-"*50)

# EXERCICIO 31

dis = float(input("Qual a distancia que essa viagem terá?: "))

if dis <= 200:
    print(f"O preço total da viagem será R${dis * 0.50:.2f}!")
else:
    print(f"O preço da viagem será R${dis * 0.45:.2f}!")

