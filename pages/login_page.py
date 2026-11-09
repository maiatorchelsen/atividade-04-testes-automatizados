"""Page Object da página de login e cadastro do LocalEats."""

from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class LoginPage:
    """Encapsula os locators e ações da tela de login/cadastro."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.criar_conta_botao = page.get_by_role("button", name="Criar Conta")
        self.nome_input = page.get_by_role("textbox", name="Seu nome")
        self.email_cadastro_input = page.get_by_role(
            "textbox", name="novo@teste.com"
        )
        self.senha_cadastro_input = page.get_by_role(
            "textbox", name="Min. 3 caracteres"
        )
        self.registrar_botao = page.get_by_role("button", name="Registrar")
        self.email_login_input = page.get_by_role(
            "textbox", name="teste@teste.com"
        )
        self.senha_login_input = page.get_by_role(
            "textbox", name="Sua senha secreta"
        )
        self.entrar_botao = page.locator("#loginForm").get_by_role(
            "button", name="Entrar"
        )

    def abrir(self) -> None:
        """Abre a página de login."""
        self.page.goto(f"{BASE_URL}/login.html")

    def abrir_cadastro(self) -> None:
        """Exibe o formulário de criação de conta."""
        self.criar_conta_botao.click()

    def preencher_cadastro(self, nome: str, email: str, senha: str) -> None:
        """Preenche os dados do formulário de cadastro."""
        self.nome_input.fill(nome)
        self.email_cadastro_input.fill(email)
        self.senha_cadastro_input.fill(senha)

    def enviar_cadastro(self) -> None:
        """Envia o formulário de cadastro."""
        self.registrar_botao.click()

    def criar_conta(self, nome: str, email: str, senha: str) -> None:
        """Executa o fluxo completo de criação de conta."""
        self.abrir_cadastro()
        self.preencher_cadastro(nome, email, senha)
        self.enviar_cadastro()

    def preencher_login(self, email: str, senha: str) -> None:
        """Preenche as credenciais de login."""
        self.email_login_input.fill(email)
        self.senha_login_input.fill(senha)

    def enviar_login(self) -> None:
        """Envia o formulário de login."""
        self.entrar_botao.click()

    def entrar(self, email: str, senha: str) -> None:
        """Executa o fluxo completo de login."""
        self.preencher_login(email, senha)
        self.enviar_login()
