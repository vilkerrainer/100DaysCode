"""
Funções com parâmetros padrão e args:
TODO: Faça uma função que receba qualquer quantidade de números e retorne a média deles. Se não receber nada, retorne 0.
"""
import random

def media(quantidade, escolha):
    
    lista_nums = []
    
    if escolha == 1:

        for i in range(quantidade):
            i += 1
            nums = int(input(f"Digite {i}º o número: "))
            lista_nums.append(nums)   

    elif escolha == 2:        
        for i in range(quantidade):
                i += 1
                rand_nums = random.randrange(1, 100)
                lista_nums.append(rand_nums)

    valor = 0

    for numeros in lista_nums:
         valor = valor + numeros

    return f"A média de {lista_nums} é igual a {valor / quantidade}"

while True:
    try:        
        quantidade = int(input("Você quer a média de quantos números?: ")) 
        
        if quantidade == 0:
            print(0)
            break
        else:
            escolha = int(input("Você quer digitar os números ou quer números aleatórios?\n" \
                        "1 - Digitar números\n" \
                        "2 - Números aleatórios\n" \
                        "Escolha: "))
            print(media(quantidade, escolha))
            break
    except:
        print("Por favor digite um número")
