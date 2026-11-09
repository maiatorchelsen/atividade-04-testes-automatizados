"""Regras de negócio automatizadas do LocalEats."""


def quantidade_itens_valida(quantidade):
    """Valida se a quantidade de itens de um pedido está entre 1 e 10.

    Retorna ``True`` para quantidades de 1 a 10, ``False`` para zero ou
    valores acima de 10 e gera ``ValueError`` para quantidades negativas.
    """
    if quantidade < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")
    return 1 <= quantidade <= 10
