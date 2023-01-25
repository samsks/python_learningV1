def fundamentals():
    # Literal
    my_lst = [1, 'String', True, 3.8, ['outra', 'lista']]
    print(type(my_lst))
    print(my_lst)

    # Builtin
    my_lst_2 = list('uma string')
    # print(type(my_lst_2))
    # print(my_lst_2)

    # Tamanho
    # print(len(my_lst_2))

    # Acessando elementos
    # print(my_lst[0])
    # print(my_lst[-1])
    # print(my_lst[-1][0])
    # Slicing
    # print(my_lst[1:3])
    # print(my_lst)

    # Objetos mutáveis
    my_lst[0] = 'Novo Valor'
    # print(my_lst)

    # Métodos
    my_lst.append('ultimo item')
    print(my_lst)

    # Remove e retorna o removido
    popped_item = my_lst.pop()
    print(my_lst)
    print(popped_item)
    my_lst_3 = []
    # [].pop()
    # my_lst_3.pop()

    # Remove todos os elementos da lista
    my_lst.clear()
    print(my_lst)

    print(my_lst.append(2))
    print(my_lst)
