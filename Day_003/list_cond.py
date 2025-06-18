"""
List Comprehension + Condições:
TODO: Gere uma lista com todos os números entre 1 e 200 que sejam divisíveis por 3 ou 5, mas não por ambos.
"""

lista_um_a_duzentos = []

for i in range(200):
    i += 1
    lista_um_a_duzentos.append(i)

def div_tres_cinco(lista):
    lista_correta = [i for i in lista if (i % 3 == 0) ^ (i % 5 == 0)]
    print(lista_correta)

div_tres_cinco(lista_um_a_duzentos)