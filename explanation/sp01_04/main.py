from data_types import strings, lists, tuples, sets, dicts, functions
from references import mutability, packing_unpacking, comprehensions


def printing_data_types():
    # strings.fundamentals()

    # lists.fundamentals()
    # res = lists.looping()
    # print(res)

    # tuples.fundamentals()
    # tuples.looping()

    # sets.fundamentals()
    # sets.looping()

    # dicts.fundamentals()
    # dicts.looping()

    # res = functions.check_credentials('chrystian', '1234')
    # res = functions.check_credentials(3.8, '1234')
    # res = functions.check_credentials('1234', 'chrystian')
    # res = functions.check_credentials(password='1234', username='chrystian')
    # print(res)
    functions.module_greetings('bom dia', 10)


def printing_references():
    # Imutável (inteiro)
    # my_int = 10
    # print(f'antes de chamar ref_int {my_int}')
    # mutability.ref_int(10)
    # print(f'depois de chamar ref_int {my_int}')

    # Mutável (lista)
    # my_list = [1, 2, 3]
    # print(f'antes de chamar ref_list {my_list}')
    # mutability.ref_list(my_list)
    print(f'depois de chamar ref_list {my_list}')


def printing_packing_unpacking():
    # packing_unpacking.func_args()
    # packing_unpacking.func_args(1, 2, 3)
    my_list = [10, 20, 30]
    my_set = {10, 20, 30}
    # packing_unpacking.func_args(*my_list)
    # packing_unpacking.func_args(my_list)

    # packing_unpacking.func_kwargs()
    my_dict = {'username': 'chrystian', 'password': '1234'}
    my_dict2 = {'username2': 'gustavo', 'password2': '1234'}
    packing_unpacking.func_kwargs(**my_dict, **my_dict2)
    # packing_unpacking.func_kwargs()
    # print(my_dict)
    # packing_unpacking.func_kwargs(username=my_dict['username'], password=my_dict['password'])

    # packing_unpacking.func_args(*my_set)
    packing_unpacking.func_kwargs(**my_list)


def printing_comprehensions():
    res = comprehensions.list_c()
    print(res)


def main():
    # printing_data_types()
    # printing_references()
    # printing_packing_unpacking()
    printing_comprehensions()


if __name__ == '__main__':
    main()
