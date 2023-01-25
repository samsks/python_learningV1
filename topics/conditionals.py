# if
numero_one = 10
if numero_one > 0:
    print("numero é positivo")

# if and elif(else if)
numero_two = 10
if numero_two > 0:
    print("numero é positivo")
elif numero_two < 0:
    print("numero é negativo")

# if, elif and else
numero_three = 10
if numero_three > 0:
    print("numero é positivo")
elif numero_three < 0:
    print("numero é negativo")
else:
    print("numero é zero")


# Operadores relacionais
# ==: igualdade (retorna True se os valores forem iguais, False
# caso contrário)

# !=: diferente (retorna True se os valores forem diferentes, False
# caso contrário)

# >: maior que (retorna True se o valor à esquerda for maior que o
# valor à direita, False caso contrário)

# <: menor que (retorna True se o valor à esquerda for menor que o
# valor à direita, False caso contrário)

# >=: maior ou igual a (retorna True se o valor à esquerda for maior
# ou igual ao valor à direita, False caso contrário)

# <=: menor ou igual a (retorna True se o valor à esquerda for menor
# ou igual ao valor à direita, False caso contrário)

# Exemplos
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True


# Operadores Lógicos

# and: retorna verdadeiro se ambas as expressões forem verdadeiras
# or: retorna verdadeiro se pelo menos uma das expressões for verdadeira
# not: inverte o valor lógico da expressão

# Exemplos
a = 10
b = 20
c = 30

print(a < b and b < c)  # True
print(a < b or b > c)   # True
print(not (a == b))     # True
