"""
Programação Funcional: reduce():
TODO: Use reduce() para calcular o produto de uma lista de números.
"""
from functools import reduce

numeros = [2, 3, 4]
produto = reduce(lambda x, y: x * y, numeros)
print(f"resultado: {produto}")
