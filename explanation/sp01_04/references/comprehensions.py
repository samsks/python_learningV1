def list_c() -> list:
    # Caso 1
    # numbers = []

    # for number in range(1, 6):
    #     numbers.append(number)
    # Ex Caso 1
    # return numbers
    # Equivalente a um map
    # res = [number for number in range(1, 6)]
    # return res

    # Caso 2
    # numbers = []

    # for number in range(1, 6):
    #     if number % 2 == 0:
    #         numbers.append(number)

    # return numbers
    # Equivalente a um filter
    # return [number for number in range(1, 6) if number % 2 == 0]

    # Caso 3
    # numbers = []

    # for number in range(1, 6):
    #     if number % 2 == 0:
    #         numbers.append('par')
    #     else:
    #         numbers.append('impar')

    # return numbers

    # return ["par" if number % 2 == 0 else "impar" for number in range(1, 6)]
    # return [number * 100 for number in range(1, 6)]

    users = [
        {'name': 'chrystian', 'module': 'm5'},
        {'name': 'rapha', 'module': 'm5'},
        {'name': 'fabio', 'module': 'm4'},
        {'name': 'cauan', 'module': 'm4'},
    ]

    m5_users = [user['name'] for user in users if user['module'] == 'm5']

    # m5_users = []

    # for user in users:
    #     if user['module'] == 'm5':
    #         m5_users.append(user)

    return m5_users

    # return [number for number in range(1, 6) if number % 2 == 0]

    # match
