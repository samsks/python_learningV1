def ref_int(number: int) -> None:
    number = 200
    print(f'dentro de ref_int {number}')


def ref_list(lista: list) -> None:
    lista[0] = 'Novo Valor'
    print(f'dentro de ref_list {lista}')
