"""Testes BDD do login de usuário."""

from playwright.sync_api import Page, expect
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from pages.login_page import BASE_URL, LoginPage
from tests.fixtures import credenciais, dados_cadastro


@scenario("../features/login.feature", "Login com sucesso")
def test_login_com_sucesso():
    """Login com sucesso."""


@given("que a página de login está disponivel")
def pagina_de_login(page: Page) -> None:
    """Abre a página de login."""
    LoginPage(page).abrir()


@when("adiciono credenciais válidas")
def preencho_credenciais(page: Page, credenciais: dict[str, str]) -> None:
    """Preenche as credenciais geradas para o cenário."""
    LoginPage(page).preencher_login(credenciais["email"], credenciais["senha"])


@when('clicar no botão "Entrar"')
def clico_em_entrar(page: Page) -> None:
    """Envia o formulário de login."""
    LoginPage(page).enviar_login()


@then("devo ser redirecionado a página principal")
def verifico_pagina_principal(page: Page) -> None:
    """Verifica o redirecionamento após o login."""
    expect(page).not_to_have_url(f"{BASE_URL}/login.html")
