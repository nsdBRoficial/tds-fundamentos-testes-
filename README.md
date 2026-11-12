# 📚 Teoria e Prática: Fundamentos de Testes de Software

Sejam bem-vindos à atividade prática sobre os princípios teóricos de testes.

---

## 📖 1. Guia Teórico Rápido

Antes de codificar, leia estes conceitos essenciais:

1. **O que é um Teste de Software?**
   É a execução controlada de um programa para verificar se o comportamento observado coincide com o comportamento esperado (*Expected Result vs. Actual Result*).

2. **Caminho Feliz (Happy Path):**
   É o cenário padrão, onde os dados de entrada são válidos e o fluxo ocorre sem imprevistos.
   *Exemplo:* Passar `[8.0, 9.0]` para calcular média e receber `8.5`.

3. **Casos de Borda (Boundary Testing):**
   Testar os valores limites onde a lógica costuma falhar.
   *Exemplo:* O que acontece com a nota `7.0` exata? Ela cai em "Aprovado" ou "Recuperação"?

4. **Tratamento de Exceções:**
   Testar se o programa falha de forma segura quando recebe dados incorretos, em vez de quebrar silenciosamente.
   *Exemplo:* Passar lista vazia ou nota `-1`.

5. **Asserção (`assert`):**
   Uma instrução que verifica se uma condição é verdadeira. Se for falsa, interrompe a execução com erro.
   *Exemplo:* `assert classificar_aluno(8.0) == "Aprovado"`

---

## 🎯 2. O Desafio da Aula (Duração: 1h30 a 2h)

Cada aluno deve:
1. Criar uma cópia do arquivo modelo dentro da pasta `respostas/` com o nome `resposta_<seu_nome>.py`.
2. Responder a **3 perguntas conceituais** em forma de comentários no código.
3. Escrever **3 blocos de testes manuais com `assert`** cobrindo os conceitos explicados acima.

---

## 📝 3. Modelo do Arquivo (`respostas/resposta_<seu_nome>.py`)

Copie a estrutura abaixo para criar o seu arquivo:

```python
from exercicio import calcular_media, classificar_aluno, dividir_premio

# ==========================================
# PARTE 1: TEORIA (Responda com suas palavras)
# ==========================================

# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta: 

# 2. Qual a diferença entre um teste de "Caminho Feliz" e um teste de "Caso de Borda"?
# Resposta:

# 3. Na função 'classificar_aluno', quais são os valores críticos de borda que você DEVE testar?
# Resposta:


# ==========================================
# PARTE 2: IMPLEMENTAÇÃO DOS TESTES COM ASSERT
# ==========================================

def testar_tudo():
    print("Iniciando testes...")

    # TESTE 1: Caminho Feliz
    # Verifique se o cálculo da média com [6.0, 8.0] retorna 7.0
    assert calcular_media([6.0, 8.0]) == 7.0, "Erro no cálculo da média básica"

    # TESTE 2: Casos de Borda (Classificação)
    # Teste exatamente a borda 5.0 e a borda 7.0
    assert classificar_aluno(7.0) == "Aprovado", "Borda 7.0 deveria aprovar"
    assert classificar_aluno(5.0) == "Recuperação", "Borda 5.0 deveria deixar em recuperação"

    # TESTE 3: Tratamento de Exceção
    # Teste se dividir o prêmio por 0 gera ZeroDivisionError
    try:
        dividir_premio(1000.0, 0)
        assert False, "Deveria ter lançado ZeroDivisionError"
    except ZeroDivisionError:
        pass # Comportamento correto esperado!

    print("✅ Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    testar_tudo()
```

---

## 🚀 4. Como Entregar

1. Clone o repositório:
```bash
git clone https://github.com/nsdBRoficial/tds-fundamentos-testes.git
cd tds-fundamentos-testes
```

2. Crie sua branch:
```bash
git checkout -b entrega-<seu_nome>
```

3. Crie e preencha `respostas/resposta_<seu_nome>.py`.
4. Execute no terminal para ver se seus testes rodam:
```bash
python respostas/resposta_<seu_nome>.py
```

5. Comite e abra o Pull Request:
```bash
git add respostas/resposta_<seu_nome>.py
git commit -m "docs e testes: entrega teorica de <seu_nome>"
git push origin entrega-<seu_nome>
```

6. Abra o Pull Request no GitHub com o título: `[ENTREGA] - <Seu Nome>`.

