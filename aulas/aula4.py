# MODULOS
# é a funcionalidade de importar funçoes extras
# com "import ..." ou "from ... import ..."
import math
num = int(input("digite um numero: "))
raiz = math.sqrt(num)
print(f"a raiz de {num} é igual a {raiz:.2f}")

# OU

from math import sqrt
num = int(input("digite um numero: "))
raiz = sqrt(num)
print(f"a raiz de {num} é igual a {raiz:.2f}")
 
