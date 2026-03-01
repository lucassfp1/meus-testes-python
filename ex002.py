valor = input("digite algo: ")

print("o tipo primitivo desse valor é", type(valor))

print("só tem espaços?", valor.isspace())
print("é um número?", valor.isnumeric())
print("é alfabético?", valor.isalpha())
print("é alfanumérico?", valor.isalnum())
print("está em maiúsculas?", valor.isupper())
print("está em minúsculas?", valor.islower())
print("está capitalizada?", valor.istitle())
