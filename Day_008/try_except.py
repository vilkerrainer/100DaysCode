"""
Exceções (try/except):
TODO: Faça um programa que receba um número do usuário e trate o erro caso não seja um número válido, pedindo para tentar novamente.
"""

while True:  
    try:
        n1 = int(input("Digite um número: "))
        print(f"O número escolhido foi: {n1}")
        break
    except:
        print("Por favor digite um número")
        