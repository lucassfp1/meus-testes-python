# exercicio 16

from math import floor

print("-"*40)
num = float(input("Cite um número quebrado: "))
print(f"O número {num} possui {floor(num)} unidades inteiras!")
print("-"*40)

# exercicio 17

from math import hypot

print("-"*40)
a = float(input("Qual o comprimento do cateto oposto do triangulo? "))
b = float(input("Qual o comprimento do cateto adjacente do triangulo? "))
hyp = hypot(a, b)
print(f"A hipotenusa desse triangulo retangulo mede {hyp:.2f}!")
print("-"*40)

# exercicio 18

from math import sin, cos, tan, radians

print("-"*40)
angle = float(input("Qual o angulo? "))
rad = radians(angle)

print(f"O angulo {angle} desse circulo tem:")
print(f"{sin(rad):.2f} de seno,")
print(f"{cos(rad):.2f} de cosseno,")
print(f"{tan(rad):.2f} de tangente!")
print("-"*40)
