"""Testes funcionais da interface do LocalEats."""

from pathlib import Path

from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import BASE_URL, LoginPage
from tests.fixtures import dados_cadastro

EVIDENCIAS_DIR = Path(__file__).resolve().parents[1] / "evidencias"


def test_cadastro_permite_visualizar_restaurantes(
    page: Page, dados_cadastro: dict[str, str]
) -> None:
    """Após criar uma conta, o usuário deve visualizar a lista de restaurantes."""
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.abrir()
    login_page.criar_conta(
        dados_cadastro["nome"],
        dados_cadastro["email"],
        dados_cadastro["senha"],
    )

    expect(page).to_have_url(f"{BASE_URL}/index.html")
    expect(home_page.titulo).to_be_visible()
    expect(home_page.primeiro_restaurante).to_be_visible()

    EVIDENCIAS_DIR.mkdir(exist_ok=True)
    page.screenshot(
        path=str(EVIDENCIAS_DIR / "home-restaurantes.png"),
        full_page=True,
    )
