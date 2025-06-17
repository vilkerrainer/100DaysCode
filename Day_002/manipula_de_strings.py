"""
Manipulação de Strings:
TODO: Crie uma função que receba uma string e retorne um dicionário com a contagem de cada caractere, ignorando espaços e maiúsculas/minúsculas.
"""

palavra = "texto muito grande"

def teste(palavra):
    palavra = palavra.replace(" ", "").lower()
    letras_em_lista = []

    for i in range(len(palavra)):
        letras_em_lista.append(palavra[i])

    contagem_letras = {}

    for letra in letras_em_lista:
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
    
    return contagem_letras

print(teste(palavra))
