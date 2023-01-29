def fundamentals():
    # Literal
    my_dict = {
        "chave": "valor_1",
        1: True,
        "chave_2": "valor_2",
        "chave": "valor_3"
    }
    print(type(my_dict))
    print(my_dict)
    print()

    # Acessando valores
    # Mutável
    # print(my_dict["chave"])
    # # print(my_dict.chave)
    # my_dict['chave_1000'] = 'valor 1000'
    # print(my_dict)
    # my_dict['chave_1000'] = 'novo valor'
    # print(my_dict)

    # my_dict['chave_5000']
    # my_value = my_dict.get('chave_5000', "CHAVE NAO ENCONTRADA")
    # print(my_value)

    my_dict.update({"nova_chave": 1000, "chave": "valor atualizado"})
    print(my_dict)

    my_dict_2 = {"username": "chrystian", "addresses": ["rua 1", "rua 2"]}
    print(my_dict_2["addresses"][1])


def looping():
    print('dict original:')
    user = {
        "name": "Chrystian",
        "age": 29,
        "module": "M5"
    }
    print(user)
    print()

    # print('.keys()')
    # print(user.keys())
    # print(type(user.keys()))
    # print(list(user.keys()))
    # print(tuple(user.keys()))
    # print(set(user.keys()))
    # print()

    # print('.values()')
    # print(user.values())
    # print(type(user.values()))
    # print(list(user.values()))
    # print(tuple(user.values()))
    # print(set(user.values()))
    # print()

    print('.items()')
    print(user.items())
    print(type(user.items()))
    print(list(user.items()))
    print(tuple(user.items()))
    print(set(user.items()))
    print()

    # for key in user.keys():
    #     print(f'CHAVE -> {key}')

    # for value in user.values():
    #     print(f'VALOR -> {value}')

    # for k, v in user.items():
    #     print(f'{k} / {v}')
    #     print(f'ITEM -> {item}')

    for index, key in enumerate(user):
        print(user[key])
        # print(f'{index} - {key}')
