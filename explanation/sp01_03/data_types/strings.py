"""
    Comentario
    multi
    linha
"""
# print('__name__ strings.py -> ', __name__)


def fundamentals():
    x = 'bom dia'
    y = '5'
    z = """Um texto
        multilinha
        qualquer
    """

    MY_CONST = 10

    # print(x)
    # print(y)
    # print(z)

    # `${}`
    template_str = f'Boa tarde M{y}'
    # print(template_str)
    template_str_2 = f'{x} M{y}'
    # print(template_str_2)

    # print(template_str[0])
    # print(len(template_str))
    str_len = len(template_str)
    # print(template_str[str_len - 1])
    # print(template_str[-1])
    # print(template_str[-2])

    # Strings são objetos imutáveis
    template_str = f'  Boa tarde M5  '
    # splice
    print(template_str)

    # template_str[0] = 'Z'

    # Slicing / Fatiamento
    # print(template_str[2:7])
    # [start:stop:step]
    # print(template_str[:7])
    # print(template_str[2:])
    # print(template_str[:])
    # print(template_str[2:10:2])
    # print(template_str[::-1])

    # SPLIT
    str_split = template_str.split()
    # print(str_split)

    # JOIN
    str_join = "$".join(str_split)
    # print(str_join)

    # print(list(template_str))

    print(template_str.strip())
    print(template_str.replace(" ", ""))
