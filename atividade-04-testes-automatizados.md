# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

- **Turma:** Qualidade software 2026-2 Noite
- **Modalidade:** Individual
- **Repositório:** https://github.com/maiatorchelsen/atividade-04-testes-automatizados
- **Diretório da atividade:** (https://github.com/lucianozanuz/pbl-qualidade-software-2026-2/blob/main/atividades/atividade-04/atividade-04-testes-automatizados.md)
- **Data da última execução:** 09/11/2026

### Integrantes

1. Maiara Torchelsen Saraiva

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Maiara Torchelsen Saraiva | Unitário | Quantidade entre 1 e 10 retorna `True` | `tests/test_regras_localeats.py::test_quantidade_dentro_do_limite_retorna_true` |
| TU02 | Maiara Torchelsen Saraiva | Unitário | Quantidade acima de 10 retorna `False` | `tests/test_regras_localeats.py::test_quantidade_acima_do_limite_retorna_false` |
| TU03 | Maiara Torchelsen Saraiva | Unitário | Quantidade igual a zero retorna `False` | `tests/test_regras_localeats.py::test_quantidade_zero_retorna_false` |
| TU04 | Maiara Torchelsen Saraiva | Unitário | Quantidade igual a 1 retorna `True` | `tests/test_regras_localeats.py::test_quantidade_um_retorna_true` |
| TU05 | Maiara Torchelsen Saraiva | Unitário | Quantidade igual a 10 retorna `True` | `tests/test_regras_localeats.py::test_quantidade_dez_retorna_true` |
| TU06 | Maiara Torchelsen Saraiva | Unitário | Quantidade negativa gera `ValueError` | `tests/test_regras_localeats.py::test_quantidade_negativa_gera_value_error` |
| TF01 | Maiara Torchelsen Saraiva | Funcional | Cadastro de usuário e visualização dos restaurantes na página inicial | `tests/test_localeats.py::test_cadastro_permite_visualizar_restaurantes` |

### Quantidades mínimas

- **Individual:** uma função, dois testes unitários e um teste funcional.

Foram entregues uma função, seis testes unitários (dois obrigatórios e quatro diferenciais) e um teste funcional com três assertions.

---

## 3. Testes unitários

### Regra 3: quantidade de itens

```python
quantidade_itens_valida(quantidade)
```

- Retorna `True` para quantidades entre 1 e 10.
- Retorna `False` para zero ou quantidades acima de 10.
- Gera `ValueError` para quantidades negativas.

### Registro da regra implementada

#### Regra de Maiara Torchelsen Saraiva

- **Regra escolhida:** Regra 3 — quantidade de itens.
- **Função implementada:** `quantidade_itens_valida`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:**
  - `test_quantidade_dentro_do_limite_retorna_true`
  - `test_quantidade_acima_do_limite_retorna_false`
  - `test_quantidade_zero_retorna_false`
  - `test_quantidade_um_retorna_true`
  - `test_quantidade_dez_retorna_true`
  - `test_quantidade_negativa_gera_value_error`
- **Comportamentos verificados:** aceitação de quantidade válida, limites inferiores e superiores (1 e 10), rejeição de quantidade acima do limite, rejeição de quantidade zero e exceção para quantidade negativa.

Os testes são independentes, possuem nomes descritivos, utilizam `assert` e `pytest.raises`, executam com `pytest` e identificam a responsável no código.

---

## 4. Aplicação do TDD

### TDD de Maiara Torchelsen Saraiva

- **Regra escolhida:** Regra 3 — quantidade de itens.
- **Primeiro teste escrito:** `test_quantidade_dentro_do_limite_retorna_true`
- **Por que o teste falhou inicialmente:** a função `quantidade_itens_valida` ainda não existia em `src/regras_localeats.py`, portanto a importação falhava.
- **Implementação mínima realizada:** criação da função retornando `1 <= quantidade <= 10`.
- **Segundo teste escrito:** `test_quantidade_acima_do_limite_retorna_false`
- **Melhoria ou refatoração realizada:** foram acrescentados os testes de borda para 0, 1, 10 e para quantidade negativa. A implementação foi ajustada para lançar `ValueError` antes da verificação do intervalo e o código foi organizado com docstring.

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de Maiara Torchelsen Saraiva

- **ID:** `TF01`
- **Fluxo automatizado:** criação de conta e visualização da página inicial com restaurantes.
- **Interação realizada:** abertura da página de login, clique em “Criar Conta”, preenchimento de nome, e-mail e senha, e clique em “Registrar”.
- **Primeira assertion:** verifica se a URL foi alterada para `/static/index.html` após o cadastro.
- **Segunda assertion:** verifica se o título “Descubra sabores incríveis na sua cidade” está visível.
- **Terceira assertion:** verifica se o primeiro card de restaurante foi exibido.
- **Arquivo e função:** `tests/test_localeats.py::test_cadastro_permite_visualizar_restaurantes`
- **Page Objects:** `pages/login_page.py` e `pages/home_page.py`
- **Evidência:** `evidencias/home-restaurantes.png`
- **Resultado final:** aprovado.

O teste utiliza Page Object Model, locators do Playwright, não utiliza `time.sleep`, utiliza a fixture `dados_cadastro` para gerar um e-mail único a cada execução e manter a independência e identifica a responsável no código.

---

## 6. Resultado da execução

Execução realizada no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

- **Quantidade total de testes:** 9
- **Testes aprovados:** 9
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram aprovados.

---

## 7. Explicações individuais

### Explicação do teste de Maiara Torchelsen Saraiva

- **Teste escolhido:** `test_quantidade_negativa_gera_value_error`
- **Comportamento verificado:** uma quantidade negativa deve ser rejeitada com `ValueError`.
- **Dados ou estado inicial:** a função recebe o valor `-1`.
- **Resultado esperado:** a exceção `ValueError` é lançada.
- **O que faria o teste falhar:** a função retornar `False` em vez de lançar a exceção, ou aceitar o valor negativo como válido.

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** opencode.
- **Como a ferramenta foi utilizada:** apoio na estruturação dos arquivos, na implementação inicial da função, revisão do relatório.
- **Uma sugestão que precisou ser alterada ou rejeitada:** o uso de um e-mail fixo no teste funcional.
- **Motivo da alteração ou rejeição:** um e-mail fixo poderia causar conflito entre execuções; foi adotado um e-mail único gerado com `uuid`.
- **Como o código sugerido foi verificado:** revisão do código, execução dos testes unitários e do teste funcional com Playwright e execução completa da suíte com `pytest`.

---

## 9. Diferenciais opcionais

- [x] Terceiro teste unitário para caso de borda.
- [x] Uso de `pytest.raises` para verificar exceção.
- [ ] Parametrização com `pytest.mark.parametrize`.
- [x] Cenário BDD em Gherkin.
- [x] Automação com `pytest-bdd`.
- [x] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [x] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

- **Testes unitários adicionais:** `test_quantidade_zero_retorna_false`, `test_quantidade_um_retorna_true`, `test_quantidade_dez_retorna_true` e `test_quantidade_negativa_gera_value_error` cobrem casos de borda da Regra 3.
- **`pytest.raises`:** utilizado em `test_quantidade_negativa_gera_value_error`.
- **Cenário BDD em Gherkin:** `features/quantidade_itens.feature` descreve os cenários de quantidade válida, acima do limite e negativa.
- **Automação com `pytest-bdd`:** os fluxos de login e cadastro são automatizados em `tests/test_login_steps.py` e `tests/test_cadastrar_steps.py`, usando os arquivos `features/login.feature` e `features/cadastrar.feature`.
- **Fixtures compartilhadas:** `tests/fixtures.py` define `dados_cadastro` (gera nome, e-mail e senha únicos) e `credenciais` (cria o usuário via API e retorna as credenciais). Elas são importadas e reutilizadas por `test_login_steps.py`, `test_cadastrar_steps.py` e `test_localeats.py`.
- **Screenshot com Playwright:** o teste funcional gera a evidência `evidencias/home-restaurantes.png` ao final da execução.
- **Page Object Model:** os locators e ações das telas foram encapsulados em `pages/login_page.py` (`LoginPage`) e `pages/home_page.py` (`HomePage`). O `LoginPage` é reutilizado pelo teste funcional `test_localeats.py`, por `test_cadastrar_steps.py` e por `test_login_steps.py`, eliminando a duplicação de locators e ações de login/cadastro.

---
