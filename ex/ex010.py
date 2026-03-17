# EXERCICIO 28

from random import randint

num = int(input("Pensei em um número de 0 a 5, tente acertar!: "))
ran = randint(0,5)

if num == ran:
    print("Voce acertou parabéns!")
else:
    print("Voce errou, tente novamente!")
print("-"*50)

# EXERCICIO 29

km = float(input("Qual a velocidade atingida pelo carro?: "))
multa = (km - 80) * 7

if km > 80.0:
    print(f"A sua velocidade de {km}km/h ultrapassou os limites! Voce receberá uma multa de R${multa:.2f}!")
else:
    print(f"A sua velocidade de {km}km/h nao ultrapassou os limites, boa viagem!") 


