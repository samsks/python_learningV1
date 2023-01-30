def example_1() -> list:
    lista = [1, 2, 3]
    my_dict = {'username': 'chrystian'}
    # print(lista[0])
    try:
        print(lista[1])
    # except (IndexError, KeyError):
    except IndexError:
        return 'IndexError tratado'

    try:
        print(my_dict['chave_nao_existe'])
    except KeyError:
        return 'KeyError tratado'

    return lista


def example_2(user: dict) -> None:
    if "password" in user.keys():
        raise KeyError('chave password encontrada no dicionário')
