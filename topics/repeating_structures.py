# for

# imprime cada elemento da lista
for elemento in [1, 2, 3]:
    print(elemento)

# imprime cada caractere da string
for caractere in "Olá, mundo!":
    print(caractere)

# imprimindo os números de 1 a 5
for i in range(1, 6):
    print(i)


# while

# imprimindo os números de 1 a 5
y = 1
while y <= 5:
    print(y)
    y += 1


# Auxiliares - break and continue

# imprimindo os números de 1 a 5, mas interrompendo o laço quando o número é 3
for r in range(1, 6):
    if r == 3:
        break
    print(r)

# imprimindo os números de 1 a 5, pulando o número 3
for p in range(1, 6):
    if p == 3:
        continue
    print(p)
