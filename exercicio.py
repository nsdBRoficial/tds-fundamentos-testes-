"""
Módulo: Calculadora Financeira Simples
Utilizado para estudo de casos de teste, asserções e tratamento de erros.
"""


def calcular_media(notas: list) -> float:
    """Calcula a média aritmética de uma lista de notas de 0 a 10."""
    if not isinstance(notas, list):
        raise TypeError("O parâmetro deve ser uma lista.")
    if len(notas) == 0:
        return 0.0
    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError("As notas devem estar entre 0 e 10.")
    return sum(notas) / len(notas)


def classificar_aluno(media: float) -> str:
    """Classifica a situação do aluno com base na média."""
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def dividir_premio(valor_total: float, participantes: int) -> float:
    """Divide um prêmio em dinheiro igualmente entre participantes."""
    if participantes <= 0:
        raise ZeroDivisionError("O número de participantes deve ser maior que zero.")
    return valor_total / participantes

