"""Testes unitários das regras de negócio do LocalEats."""

import pytest

from src.regras_localeats import quantidade_itens_valida


def test_quantidade_dentro_do_limite_retorna_true():
    """Uma quantidade entre 1 e 10 deve ser considerada válida."""
    assert quantidade_itens_valida(3) is True


def test_quantidade_acima_do_limite_retorna_false():
    """Uma quantidade acima de 10 deve ser considerada inválida."""
    assert quantidade_itens_valida(11) is False


def test_quantidade_zero_retorna_false():
    """Uma quantidade igual a zero deve ser considerada inválida."""
    assert quantidade_itens_valida(0) is False


def test_quantidade_um_retorna_true():
    """Uma quantidade igual a 1 deve ser considerada válida."""
    assert quantidade_itens_valida(1) is True


def test_quantidade_dez_retorna_true():
    """Uma quantidade igual a 10 deve ser considerada válida."""
    assert quantidade_itens_valida(10) is True


def test_quantidade_negativa_gera_value_error():
    """Uma quantidade negativa deve gerar ValueError."""
    with pytest.raises(ValueError):
        quantidade_itens_valida(-1)
