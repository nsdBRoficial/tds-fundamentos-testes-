from exercicio import calcular_media, classificar_aluno, dividir_premio

# ==========================================
# PARTE 1: TEORIA (Responda com suas palavras)
# ==========================================

# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta:
# Resposta: Porque testar na mão toda hora cansa, a gente esquece casos importantes e, quando o código cresce, fica impossível testar tudo de novo manualmente.

# 2. Qual a diferença entre um teste de "Caminho Feliz" e um teste de "Caso de Borda"?
# Resposta:  É o cenário padrão, onde os dados de entrada são válidos e o fluxo ocorre sem imprevistos. ja o  star os valores limites onde a lógica costuma falhar. Exemplo: O que acontece com a nota 7.0 exata? Ela cai em "Aprovado" ou "Recuperação"?

# 3. Na função 'classificar_aluno', quais são os valores críticos de borda que você DEVE testar?
# Resposta: o 7 be o 5


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





Caminho Feliz: tudo certinho, notas [6.0, 8.0] tem que dar média 7.0.
Casos de Borda: bem na linha de corte! Média 7.0 exata aprova? Média 5.0 exata deixa em recuperação?
Tratamento de Exceção: se tentar dividir um prêmio por 0 pessoas, o código tem que dar ZeroDivisionError (e não quebrar de forma estranha).
