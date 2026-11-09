# language: pt

Funcionalidade: cadastro de usuário
  Cenário: Cadastrar usuário com sucesso
    Dado que a página de cadastro está disponivel
    Quando adiciono os dados de cadastro
    E clicar no botão "Registrar"
    Então devo acessar a página inicial
