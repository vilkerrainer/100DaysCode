"""
Regex básico:
TODO: Escreva uma função que valide se uma string é um email válido.
"""
import re

def validar_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

print(validar_email('teste@email.com'))
print(validar_email('invalido@email'))
