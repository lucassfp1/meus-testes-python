#desafio 14

g = float(input("Quantos graus está? "))
f = (g*9/5)+32
print("-"*40)
print(f"A temperatura de {g} graus Celsius \nserá convertida em {f:.2f} grau Fahrenheit!")
print("-"*40)

#desafio 15

km = float(input("Qual a quantidade de Km percorrido? "))
dias = int(input("Qual a quantidade de dias alugados? "))
preço = (km*0.15)+(dias*60)
print("-"*50)
print(f"Pelo aluguel de {dias} dias e pela distancia de {km} KM")
print(f"O preço total a pagar será R${preço:.2f}")
print("-"*50)
