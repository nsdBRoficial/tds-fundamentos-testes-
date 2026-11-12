
from exercicio import calcular_media, classificar_aluno, dividir_premio

# ==========================================
# PARTE 1: TEORIA
# ==========================================

# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta: Porque os testes manuais podem deixar passar erros e são demorados.
# Os testes automatizados permitem repetir verificações rapidamente e com segurança.

# 2. Qual a diferença entre um teste de Caminho Feliz e um Caso de Borda?
# Resposta: Caminho Feliz testa situações comuns com dados válidos.
# Caso de Borda testa valores próximos dos limites da lógica do programa.

# 3. Na função classificar_aluno, quais são os valores críticos de borda que você DEVE testar?
# Resposta: Os valores 5.0 e 7.0, além de valores próximos, como 4.9, 5.1,
# 6.9 e 7.1.

# ==========================================
# PARTE 2: TESTES COM ASSERT
# ==========================================

def testar_tudo():
    print("Iniciando testes...")

    # TESTE 1: Caminho Feliz
    assert calcular_media([6.0, 8.0]) == 7.0, \
        "Erro no cálculo da média básica"

    # TESTE 2: Casos de Borda
    assert classificar_aluno(7.0) == "Aprovado", \
        "Borda 7.0 deveria aprovar"

    assert classificar_aluno(5.0) == "Recuperação", \
        "Borda 5.0 deveria deixar em recuperação"

    # TESTE 3: Tratamento de Exceção
    try:
        dividir_premio(1000.0, 0)
        assert False, "Deveria ter lançado ZeroDivisionError"
    except ZeroDivisionError:
        pass

    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    testar_tudo()
