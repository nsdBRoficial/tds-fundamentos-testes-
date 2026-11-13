import os
import sys

# Garante que o exercicio.py (que está na raiz do projeto) seja encontrado
# quando o arquivo é executado com: python respostas/resposta_pedro.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Evita erro ao imprimir acentos/emoji em terminais do Windows (cp1252)
sys.stdout.reconfigure(encoding="utf-8")

from exercicio import calcular_media, classificar_aluno, dividir_premio

# ==========================================
# PARTE 1: TEORIA (Responda com suas palavras)
# ==========================================

# 1. Por que não devemos confiar apenas em testes manuais executados no terminal?
# Resposta: Porque o teste manual depende de alguém lembrar de rodar e de conferir
# o resultado com o olho, e isso é lento e fácil de errar. A gente acaba esquecendo
# alguns casos, não testa sempre do mesmo jeito e, conforme o código cresce, fica
# inviável repetir tudo a cada mudança. Um teste automatizado (com assert) roda
# igual toda vez, em segundos, e avisa na hora se alguma alteração quebrou algo
# que já funcionava (regressão).

# 2. Qual a diferença entre um teste de "Caminho Feliz" e um teste de "Caso de Borda"?
# Resposta: O Caminho Feliz testa o uso "normal" da função, com dados válidos e
# comuns, para ver se ela faz o básico certo (ex: média de [6.0, 8.0] dar 7.0).
# O Caso de Borda testa os valores bem nos limites da regra, onde os erros costumam
# aparecer, como trocar um ">=" por ">" (ex: a nota 7.0 exata aprova ou não?).
# O primeiro mostra que funciona no dia a dia; o segundo mostra que as linhas de
# corte foram programadas do jeito certo.

# 3. Na função 'classificar_aluno', quais são os valores críticos de borda que você DEVE testar?
# Resposta: Os pontos de corte e os valores logo ao lado deles:
#   - 7.0  -> exatamente na borda, deve ser "Aprovado"
#   - 6.99 -> logo abaixo de 7.0, deve ser "Recuperação"
#   - 5.0  -> exatamente na borda, deve ser "Recuperação"
#   - 4.99 -> logo abaixo de 5.0, deve ser "Reprovado"
# Também vale testar os extremos da escala de notas: 0.0 ("Reprovado") e
# 10.0 ("Aprovado").


# ==========================================
# PARTE 2: IMPLEMENTAÇÃO DOS TESTES COM ASSERT
# ==========================================

def testar_tudo():
    print("Iniciando testes...")

    # TESTE 1: Caminho Feliz
    # Verifique se o cálculo da média com [6.0, 8.0] retorna 7.0
    assert calcular_media([6.0, 8.0]) == 7.0, "Erro no cálculo da média básica"
    assert calcular_media([8.0, 9.0]) == 8.5, "Média de [8.0, 9.0] deveria ser 8.5"
    assert classificar_aluno(8.5) == "Aprovado", "Média 8.5 deveria aprovar"
    assert dividir_premio(1000.0, 4) == 250.0, "1000 dividido por 4 deveria dar 250"

    # TESTE 2: Casos de Borda (Classificação)
    # Teste exatamente a borda 5.0 e a borda 7.0
    assert classificar_aluno(7.0) == "Aprovado", "Borda 7.0 deveria aprovar"
    assert classificar_aluno(5.0) == "Recuperação", "Borda 5.0 deveria deixar em recuperação"
    # Valores logo abaixo de cada borda
    assert classificar_aluno(6.99) == "Recuperação", "6.99 deveria deixar em recuperação"
    assert classificar_aluno(4.99) == "Reprovado", "4.99 deveria reprovar"
    # Extremos da escala de notas
    assert classificar_aluno(10.0) == "Aprovado", "Nota máxima 10.0 deveria aprovar"
    assert classificar_aluno(0.0) == "Reprovado", "Nota mínima 0.0 deveria reprovar"
    assert calcular_media([0.0, 10.0]) == 5.0, "Notas 0 e 10 são válidas e a média deveria ser 5.0"

    # TESTE 3: Tratamento de Exceção
    # Teste se dividir o prêmio por 0 gera ZeroDivisionError
    try:
        dividir_premio(1000.0, 0)
        assert False, "Deveria ter lançado ZeroDivisionError"
    except ZeroDivisionError:
        pass  # Comportamento correto esperado!

    # Número negativo de participantes também deve ser recusado
    try:
        dividir_premio(1000.0, -2)
        assert False, "Participantes negativos deveriam lançar ZeroDivisionError"
    except ZeroDivisionError:
        pass

    # Nota fora da faixa de 0 a 10 deve gerar ValueError
    try:
        calcular_media([8.0, -1.0])
        assert False, "Nota -1 deveria ter lançado ValueError"
    except ValueError:
        pass

    try:
        calcular_media([10.5])
        assert False, "Nota 10.5 deveria ter lançado ValueError"
    except ValueError:
        pass

    # Passar algo que não é lista deve gerar TypeError
    try:
        calcular_media("8, 9")
        assert False, "Passar texto em vez de lista deveria lançar TypeError"
    except TypeError:
        pass

    # Lista vazia não quebra: a função retorna 0.0
    assert calcular_media([]) == 0.0, "Lista vazia deveria retornar 0.0"

    print("✅ Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    testar_tudo()
