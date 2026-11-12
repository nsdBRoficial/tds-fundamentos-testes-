from exercicio import calcular_media, classificar_aluno, dividir_premio

# ==========================================
# PARTE 1: TEORIA (Responda com suas palavras)
# ==========================================

# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta: Não devemos confiar apenas em testes manuais porque pessoas se distraem, esquecem etapas e cometem erros de digitação, e além disso, testar tudo à mão leva muito tempo.

# 2. Qual a diferença entre um teste de "Caminho Feliz" e um teste de "Caso de Borda"?
# Resposta: O teste de Caminho Feliz verifica se o sistema funciona quando o usuário faz tudo certo, sem erros e seguindo o fluxo esperado. Já o teste de Caso de Borda verifica como o sistema reage a situações extremas, incomuns ou limites.

# 3. Na função 'classificar_aluno', quais são os valores críticos de borda que você DEVE testar?
# Resposta: Os valores críticos de borda que devem ser testados são "7.0" e "5.0".


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
