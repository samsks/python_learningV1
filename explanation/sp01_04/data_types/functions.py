# TYPE HINT (dica de tipagem)

def check_credentials(username: str, password: str) -> bool:
    print(f'Variável username -> {username}')
    print(f'Variável password -> {password}')

    if username == 'chrystian' and password == '1234':
        return True

    return False

    # return username == 'chrystian' and password == '1234'


def module_greetings(msg: str, module: int = 5) -> None:
    print(f'{msg} M{module}')
