def fundamentals():
    # Forma literal
    my_tuple = ("String", 3, True, ["2", 3], 3)
    print(type(my_tuple))
    print(my_tuple)

    # Builtin
    # my_tuple_2 = tuple("minha string")
    # print(type(my_tuple_2))
    # print(my_tuple_2)
    print()

    # Sequencia
    # print(my_tuple[0])
    # print(my_tuple[-1])
    # print(my_tuple[1:3])

    # Imutável
    # my_tuple[0] = "Nova String"

    # print(my_tuple.count(3))
    # print(my_tuple.index(3))
    # print(my_tuple.index(10000))


def looping():
    my_tuple = ("String", 3, True, ["2", 3], 3)

    for item in my_tuple:
        print(item)
