"""
Funções e Listas:
TODO: Escreva uma função que receba uma lista de números e retorne uma nova lista com os números ao quadrado, mas apenas os pares.
"""

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [15, 26, 32, 41, 55, 69, 72, 84, 91, 102]

def num_ao_quadrado(lista):
    num_par = []
    num_impar = []
    num_par_ao_quadrado = []

    #Separa em par e ímpar    
    for i in range(len(lista)):
        if lista[i] %2 == 0:
            num_par.append(lista[i])
        else:
            num_impar.append(lista[i])
    
    #Adiciona numeros pares ao quadrado a lista
    for i in range(len(num_par)):
        valor_ao_quadrado = num_par[i] * num_par[i]
        num_par_ao_quadrado.append(valor_ao_quadrado)

    #Retorna os números pares ao quadrado
    return num_par_ao_quadrado



print(f"Números pares ao quadrado lista 1 {num_ao_quadrado(lista1)}")
print(f"Números pares ao quadrado lista 2 {num_ao_quadrado(lista2)}")