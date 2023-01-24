# main.py
# Isso é um comentário de uma linha
"""
Isso é
um comentário
de várias linhas
"""

"""
Os tipos de dados primitivos em python são:

1. String (str)
2. Inteiro (int)
3. Decimal (float)
4. Booleano (bool)
5. Vazio (NoneType)
"""
# Declarando variáveis
minha_string = "hello"

# Verificando o tipo de uma variável
print(type(minha_string))  # output: <class 'str'>

meu_inteiro = 123
print(type(meu_inteiro))  # output: <class 'int'>

meu_decimal = 3.1415
print(type(meu_decimal))  # output: <class 'float'>

meu_booleano = True
print(type(meu_booleano))  # output: <class 'bool'>

meu_vazio = None
print(type(meu_vazio))  # output: <class 'NoneType'>

# Declarando constantes
MINHA_CONSTANTE = 'olá M5'

# Tipagem dinâmica
minha_variavel = '2'
print(type(minha_variavel))
# output: <class 'str'>
minha_variavel = '1500'

# Tipagem forte
meu_numero = 1
print(type(meu_numero))
# output: <class 'int'>

# soma = meu_numero + minha_string
# output: TypeError: unsupported operand type(s) for +: 'int' and 'str'


def minha_funcao():
    meu_valor = 1234
    return meu_valor


print(minha_funcao())
# output: 1234

print(type(minha_funcao))
# output: <class 'function'>
