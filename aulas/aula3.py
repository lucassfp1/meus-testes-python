#operadores aritméticos
#+ adição
#- subtração
#* multiplicação
#/ divisão (:.3f) para decidir as casas decimais se necessário
#// divisão inteira
#** potência ou pow()
#% resto da divisão

#ordem de precedência
#1º ()
#2º **
#3º * / // %
#4º + -

#\n pra jogar o código pra outra linha
#end=' ' para quebrar a linha

nome = input("qual é o seu nome? ")
print(f"seja bem vindo(a), {nome:20}.")
print(f"seja bem vindo(a), {nome:>20}.")
print(f"seja bem vindo(a), {nome:<20}.")
print(f"seja bem vindo(a), {nome:^20}.")

n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
print(f"a soma vale {n1 + n2}")
print(f"a subtração vale {n1-n2}")
print(f"a multiplicação vale {n1*n2}")
print(f"a divisão vale {n1/n2:.3f}")
print(f"a potência vale {n1**n2}")
print(f"a divisão inteira vale {n1//n2}")
print(f"o resto vale {n1%n2}")


n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print(f"a soma vale {s}, \na multiplicação vale {m}, \na divisão vale {n1/n2:.5f}!")
print(f"a divisão inteira vale {di} e a exponenciação vale {e}")

