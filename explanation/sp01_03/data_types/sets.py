def fundamentals():
    # Literal
    my_set = {"String", True, 3.8, ("uma", "tupla"), 10, 10, 10}

    # print(type(my_set))
    # print(my_set)
    print()
    # print(my_set[0])

    # Mutável
    # Elementos internos de um set -> imutáveis
    # my_set = {"String", True, 3.8, ["uma", "tupla"], 10, 10, 10}

    # my_set.add("novo item")
    # print(my_set)

    # my_set.remove("String")
    # print(my_set)

    my_set.update([8000, ["item set", 'outro valor']])
    print(my_set)

    my_list = [3, 3, 3, 2, 2, 1, 1, 1, 1]
    my_set_2 = set(my_list)
    # print(my_set_2)


def looping():
    my_set = {"String", True, 3.8, ("uma", "tupla"), 10, 10, 10}

    # for item in my_set:
    #     print(f'{type(item)} -> {item}')

    for index, item in enumerate(my_set):
        print(f'{index} -> {item}')