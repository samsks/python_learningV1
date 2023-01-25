
# Sintaxe - string - str
mensagem1 = 'Olá, Python!'
outra_mensagem1 = "Eu sou uma string"

mensagem2 = "Eu disse: \"Olá, mundo!\""
print(mensagem2)
# output: 'Eu disse: "Olá, mundo!"'

mensagem3 = """Este é um texto
que ocupa várias
linhas!!"""
print(mensagem3)

# Interpolação - template string

nome = 'Chrystian'
idade = 30
mensagem = f'Olá, meu nome é {nome} e eu tenho {idade} anos.'
print(mensagem)
# output: 'Olá, meu nome é João e eu tenho 30 anos.'


x = 10
y = 5

resultado = f'{x} + {y} = {x + y}'
print(resultado)
# output: '10 + 5 = 15'


# Acessando indicies

mensagem4 = 'Olá, Python!'
primeiro_caractere = mensagem4[0]
print(primeiro_caractere)
# output: 'O'

ultimo_caractere = mensagem4[-1]
print(ultimo_caractere)
# output: '!'

penultimo_caractere = mensagem4[-2]
print(penultimo_caractere)
# output: 'n'

# Fatiamento (slicing)
fatia = mensagem4[2:7]
print(fatia)
# output: 'á, P'

# Faixa que começa no início da string e vai até o terceiro
# caractere (inclusive)
fatia1 = mensagem4[:3]
print(fatia1)
# output: 'Olá'

# Faixa que começa no terceiro caractere e vai até o final da string
fatia2 = mensagem4[2:]
print(fatia2)
# output:'á, Python!'

# Métodos
# As strings em Python são objetos, o que significa que elas têm métodos e
# propriedades associados, que permitem realizar diversas operações sobre elas.
# Aqui estão alguns dos métodos mais comuns:

# upper(): converte todas as letras de uma string para maiúsculas.

# lower(): converte todas as letras de uma string para minúsculas.

# capitalize(): converte a primeira letra de uma string para maiúscula e as
# demais para minúsculas.

# title(): converte a primeira letra de cada palavra de uma string para
# maiúscula e as demais para minúsculas.

# strip(): remove espaços em branco do início e do final de uma string.

# replace(): substitui uma parte de uma string por outra.

# split(): divide uma string em uma lista de strings, usando um determinado
# delimitador.

# join(): junta uma lista de strings em uma única string, usando um
# determinado delimitador.

# find(): encontra a primeira ocorrência de uma substring em uma string e
# retorna o índice em que ela se encontra.

# count(): conta quantas vezes uma substring aparece em uma string.

# Aqui está um exemplo de como usar alguns desses métodos:

mensagem5 = ' Olá, mundo! '

# Remover os espaços em branco do início e do final da string
mensagem_limpa = mensagem5.strip()
print(mensagem_limpa)
# output: 'Olá, mundo!'

# Substituir "mundo" por "Python"
mensagem_nova = mensagem_limpa.replace('mundo', 'Python')
print(mensagem_nova)
# output: 'Olá, Python!'

# Dividir a string em uma lista de palavras
palavras = mensagem_nova.split()
print(palavras)
# output: ['Olá,', 'Python!']

# Juntar a lista de palavras em uma única string, usando um cifrão como
# delimitador
mensagem_final = '$'.join(palavras)
print(mensagem_final)
# output: 'Olá,$Python!'
