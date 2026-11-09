"""Page Object da página inicial do LocalEats."""

from playwright.sync_api import Page


class HomePage:
    """Encapsula os elementos observáveis da página inicial."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.titulo = page.get_by_role(
            "heading", name="Descubra sabores incríveis na sua cidade"
        )
        self.primeiro_restaurante = page.locator(".rest-card").first
