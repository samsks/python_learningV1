def func_args(*args: tuple) -> None:
    print(args)
    print(type(args))


def func_kwargs(**kwargs: dict) -> None:
    # kwargs['nova_chave'] = 'novo valor'
    print(kwargs)
    print(type(kwargs))
