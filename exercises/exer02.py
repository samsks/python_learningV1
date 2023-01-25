
def corresponding_parenthesis(text):
    left = text.count("(")
    right = text.count(")")
    difference = left - right

    if difference > 0:
        return "(" * difference
    elif difference < 0:
        return ")" * (difference * -1)

    return ""


# Exemplo 1
result = corresponding_parenthesis("()()")
print(result)
# ''

# Exemplo 2
result = corresponding_parenthesis("()))")
print(result)
# '))'

# Exemplo 3
result = corresponding_parenthesis(")))(((((")
print(result)
# '(('


def remove_more_than_two_repetitions(text: str):
    response = []
    response.append(text[0])
    response.append(text[1])

    for index, char in enumerate(text[2:], 2):
        if text[index - 1] != char or text[index - 2] != char:
            response.append(char)

    return "".join(response)


# Exemplo

text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)
# 'Olloco meuu, taa peegaando fogoo biichoo'
