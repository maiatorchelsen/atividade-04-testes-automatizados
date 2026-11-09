"""Testes BDD do cadastro de usuário."""

from playwright.sync_api import Page, expect
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from pages.login_page import BASE_URL, LoginPage
from tests.fixtures import dados_cadastro


@scenario("../features/cadastrar.feature", "Cadastrar usuário com sucesso")
def test_cadastrar_usuario_com_sucesso():
    """Cadastrar usuário com sucesso."""


@given("que a página de cadastro está disponivel")
def pagina_de_cadastro(page: Page) -> None:
    """Abre a página de cadastro."""
    login_page = LoginPage(page)
    login_page.abrir()
    login_page.abrir_cadastro()


@when("adiciono os dados de cadastro")
def preencho_dados_de_cadastro(
    page: Page, dados_cadastro: dict[str, str]
) -> None:
    """Preenche os dados do formulário de cadastro."""
    LoginPage(page).preencher_cadastro(
        dados_cadastro["nome"],
        dados_cadastro["email"],
        dados_cadastro["senha"],
    )


@when('clicar no botão "Registrar"')
def clico_em_registrar(page: Page) -> None:
    """Envia o formulário de cadastro."""
    LoginPage(page).enviar_cadastro()


@then("devo acessar a página inicial")
def verifico_pagina_inicial(page: Page) -> None:
    """Verifica o redirecionamento após o cadastro."""
    expect(page).to_have_url(f"{BASE_URL}/index.html")
    expect(
        page.get_by_role(
            "heading", name="Descubra sabores incríveis na sua cidade"
        )
    ).to_be_visible()
