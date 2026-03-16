# MANIPULANDO STRINGS
#   EX: frase = "Curso em Video Python"
# -Fatiamento
#   frase(9) fica "V" ou frase(9:13) fica "Vide" ou frase(9:21) "Video Python"
#   frase(9:21:2) fica "VdoPto" pois pulou de dois em dois
#   frase(:5) fica "Curso" ou frase(15:) fica "Python" ou frase(9::3) fica "VePh"

# ANALÍSE
#  len(frase), comprimento da frase = 21 char
#  frase.count('o'), contar quantas vezes = 3 'o' 
#  frase.count('o',0,13) entre o char 0 e o 13 tem apenas 1 'o'
#  frase.find("deo"), diz o momento q começou = position 11
#  frase.find("Android") = -1, ou seja nao foi encontrado
#  "Curso" in frase = True

# TRANSFORMAÇÃO 
#  frase.replace("Python","Android"), troca o primeiro pelo segundo
#  frase.upper(), troca todas minusculas para maisculas ou frase.lower(), é o contrario
#  frase.capitalize(), todos os char para minusculos exceto a primeira
#  frase.title(), analisa todas as palavras e coloca maisculas no começo delas

#  Novo exemplo = frase = "   Aprenda Python  "
#  frase.strip(), remove os espaços inuteis no começo e no final = "Aprenda Python"
#  frase.rstrip(), remove os espaços da dir. e frase.lstrip() que remove os da esq.

# DIVISAO - frase = "Curso em Video Python"
#  frase.split(), divide as palavras de acordo com os espaços "Curso" "em" "Video" "Python"

# JUNÇAO 
#   "-".join(frase) = "Curso-em-Video-Python"

frase = "Curso em Video Python"
print(frase[::2])

print(frase.count("o"))

print(len(frase))

print(frase.replace("Python", "Android"))

print(frase.split())

# OU

dividido = frase.split()
print(dividido[0])
