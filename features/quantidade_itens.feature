# language: pt

Funcionalidade: Validação da quantidade de itens do pedido
  Como cliente do LocalEats
  Quero que a quantidade de itens seja validada
  Para garantir que o pedido tenha entre 1 e 10 itens

  Cenário: Quantidade dentro do limite permitido
    Dado que informo a quantidade de 3 itens
    Quando o sistema valida a quantidade
    Então o resultado deve ser verdadeiro

  Cenário: Quantidade acima do limite permitido
    Dado que informo a quantidade de 11 itens
    Quando o sistema valida a quantidade
    Então o resultado deve ser falso

  Cenário: Quantidade negativa
    Dado que informo a quantidade de -1 itens
    Quando o sistema valida a quantidade
    Então o sistema deve informar um erro de valor
