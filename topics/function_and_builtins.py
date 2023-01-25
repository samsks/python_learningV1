def soma1(parametro1, parametro2):
    return parametro1 + parametro2


resultado = soma1(4, 5)
# parametro1 -> 4 | parametro2 -> 5
print(resultado)
# 9


def soma2(parametro1, parametro2=0):
    return parametro1 + parametro2


resultado = soma2(100)
# Usa o valor padrão de parametro2 (0)
print(resultado)
# 100


# Argumentos nomeados
def calcular_preco(preco, desconto):
    return preco * (1 - desconto)


preco_final1 = calcular_preco(preco=100, desconto=0.1)
print(preco_final1)

preco_final2 = calcular_preco(100, desconto=0.1)
print(preco_final2)

preco_final3 = calcular_preco(desconto=0.1, preco=100)
print(preco_final3)


# Auxiliar pass

# cria uma função vazia
def minha_funcao():
    pass


print(minha_funcao())


# cria uma função vazia da mesma forma
def minha_funcao2():
    ...


print(minha_funcao2())

# cria um loop vazio
for x in range(10):
    pass


# cria uma classe vazia
class MinhaClasse:
    pass


# Funções builtins

# # A
# abs()
# all()
# any()
# ascii()

# # B
# bin()
# bool()
# breakpoint()
# bytearray()
# bytes()

# # C
# callable()
# chr()
# classmethod()
# compile()
# complex()

# # D
# delattr()
# dict()
# dir()
# divmod()

# # E
# enumerate()
# eval()
# exec()

# # F
# filter()
# float()
# format()
# frozenset()

# # G
# getattr()
# globals()

# # H
# hasattr()
# hash()
# help()
# hex()

# # I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()

# # L
# len()
# list()
# locals()

# # M
# map()
# max()
# memoryview()
# min()

# # N
# next()

# # O
# object()
# oct()
# open()
# ord()

# # P
# pow()
# print()
# property()

# # R
# range()
# repr()
# reversed()
# round()

# # S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()

# # T
# tuple()
# type()

# # V
# vars()

# # Z
# zip()

# # _
# __aiter__()
# __anext__()
# __import__()


# Exemplos

# conversão de inteiro para booleano
my_bool = bool(0)
print(my_bool)
# False

# conversão de inteiro para string
my_str = str(400)
print(my_str)
# '400'

# conversão de inteiro para decimal
my_float = float(7)
print(my_float)
# 7.0

# conversão de string para inteiro
my_int = int("14")
print(my_int)
# 14

# verificar tamanho de uma estrutura sequencial
my_str = 'Kenzie Academy Brasil'
len(my_str)
# 21
