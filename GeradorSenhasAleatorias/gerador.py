import random
import string

def gerar_senha(tamanho, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Erro: Nenhum tipo de caractere selecionado!"

    return "".join(random.choice(caracteres) for _ in range(tamanho))