"""Fixtures compartilhadas pelos testes do LocalEats."""

import uuid

import pytest
from playwright.sync_api import Page

from pages.login_page import BASE_URL

API_URL = BASE_URL.removesuffix("/static")


@pytest.fixture
def dados_cadastro() -> dict[str, str]:
    """Gera dados únicos para cadastro de usuário."""
    return {
        "nome": "Teste Automatizado",
        "email": f"teste.{uuid.uuid4().hex[:10]}@example.com",
        "senha": uuid.uuid4().hex,
    }


@pytest.fixture
def credenciais(page: Page, dados_cadastro: dict[str, str]) -> dict[str, str]:
    """Cria um usuário exclusivo via API e retorna as credenciais."""
    page.request.post(
        f"{API_URL}/users/register",
        data={
            "name": dados_cadastro["nome"],
            "email": dados_cadastro["email"],
            "password": dados_cadastro["senha"],
        },
    )
    return dados_cadastro
