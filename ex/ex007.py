# exercicio 19

from random import choice

print("-"*40)
print("Olá turma, hoje será sorteado um aluno para apagar o quadro!")

stud1 = input("Qual o nome do primeiro aluno? ")
stud2 = input("Qual o nome do segundo aluno? ")
stud3 = input("Qual o nome do terceiro aluno? ")
stud4 = input("Qual o nome do quarto aluno? ")

lista = [stud1, stud2, stud3, stud4]

print(f"O aluno sorteado foi o/a {choice(lista)}!")
print("-"*40)

# exercicio 20

from random import shuffle

print("-"*40)
print("Agora irei sortear a ordem de alunos que irao apresentar o trabalho!")

aluno1 = input("Aluno 1: ")
aluno2 = input("Aluno 2: ")
aluno3 = input("Aluno 3: ")
aluno4 = input("Aluno 4: ")

lista2 = [aluno1, aluno2, aluno3 , aluno4]

shuffle(lista2)

print(f"A ordem dos alunos escolhido é:")
print(f"1º {lista2[0]}")
print(f"2º {lista2[1]}")
print(f"3º {lista2[2]}")
print(f"4º {lista2[3]}")

print("-"*40)

# exercicio 21

import pygame

pygame.init()
pygame.mixer.music.load("ex/ex007.mp3")
pygame.mixer.music.play()
pygame.event.wait()