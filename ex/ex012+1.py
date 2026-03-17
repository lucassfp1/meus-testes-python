# EXERCICIO 34
print("-=" * 30)  
sal = float(input("Qual o valor do seu salario para reajuste?: R$"))

if sal>= 1250:
    reaj = sal + (sal * 0.10)
else:
    reaj = sal + (sal * 0.15)

print(f"O seu reajuste salarial foi para R${reaj:.2f}")
print("-=" * 50)   

# EXERCICIO 35

a = float(input("Qual o comprimento dessa reta?: "))
b = float(input("Qual o comprimento dessa reta?: "))
c = float(input("Qual o comprimento dessa reta?: "))

if a + b > c and a + c > b and b + c > a:
    print(f"Essas retas formam um triangulo!")
else: 
    print(f"Essas retas nao formam um triangulo!")
print("-=" * 30)  