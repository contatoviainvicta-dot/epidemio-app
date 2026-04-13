import pandas as pd

def tabela_2x2(df):
    a = len(df[(df['exposicao'] == 1) & (df['doenca'] == 1)])
    b = len(df[(df['exposicao'] == 1) & (df['doenca'] == 0)])
    c = len(df[(df['exposicao'] == 0) & (df['doenca'] == 1)])
    d = len(df[(df['exposicao'] == 0) & (df['doenca'] == 0)])
    return a, b, c, d

def calcular_medidas(a, b, c, d):
    resultados = {}

    total = a + b + c + d

    resultados['Prevalência'] = (a + c) / total if total > 0 else 0

    ie = a / (a + b) if (a + b) > 0 else 0
    ine = c / (c + d) if (c + d) > 0 else 0

    resultados['Incidência expostos'] = ie
    resultados['Incidência não expostos'] = ine

    resultados['RR'] = ie / ine if ine > 0 else None
    resultados['OR'] = (a * d) / (b * c) if (b * c) > 0 else None

    resultados['Sensibilidade'] = a / (a + c) if (a + c) > 0 else 0
    resultados['Especificidade'] = d / (b + d) if (b + d) > 0 else 0

    resultados['VPP'] = a / (a + b) if (a + b) > 0 else 0
    resultados['VPN'] = d / (c + d) if (c + d) > 0 else 0

    return resultados
