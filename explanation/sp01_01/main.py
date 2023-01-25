# Comentário

"""
    Funções
"""


def greetings():
    return 'olá M5'

# print(type(greetings))
# print(greetings())


"""
    Tipos Primitivos
"""
# my_integer = 10
# print(type(my_integer))
# print(my_integer)

# my_float = 5.2
# print(type(my_float))
# print(my_float)

# my_string = "uma string"
# print(type(my_string))
# print(my_string)

# my_boolean = True
# print(type(my_boolean))
# print(my_boolean)

# Tipagem forte
# print(1 + '1')

"""
    Estruturas condicionais
"""

x = 4

# if x > 5:
#     print('x é maior que 5')
# elif x == 5:
#     print('x é igual a 5')
# else:
#     print('x é menor que 5')

x = 21
y = 10

# if x == 5 and y == 10:
#     print('x = 5 E y = 10')


# if x == 10 or y == 10:
#     # pass
#     print('x = 5 OU y = 10')

# if not x == 20:
#     print('x é diferente de 20')

# my_string = 'x-salada'

# if "x" in my_string:
#     print('x encontrado')

# if "y" not in my_string:
#     print('y não encontrado')

"""
    Estruturas de repetição
"""
my_string = 'olá M5!'

# for char in my_string:
#     print(char)


# for index, char in enumerate(my_string, 10):
#     # print(item)
#     # print(index)
#     print(index, char)


# for number in range(100, 110, 2):
#     print(number)

z = 0
while z < 3:
    print('loop while', z)
    z += 1
