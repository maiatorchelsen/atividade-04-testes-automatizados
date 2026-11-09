# language: pt

Funcionalidade: login de usuário 
  
  Cenário: Login com sucesso
    Dado que a página de login está disponivel
    Quando adiciono credenciais válidas
    E clicar no botão "Entrar"
    Então devo ser redirecionado a página principal
