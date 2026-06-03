import math


def media_simples(lista_de_dados):
    if not lista_de_dados:
        return 0
    
    n = len(lista_de_dados)
    soma = sum(lista_de_dados)
    
    return soma / n


def media_agrupada(elementos_x, frequencias):
    n_total = sum(frequencias)
    if n_total == 0:
        return 0
    
    soma_ponderada = sum(xi * fi for xi, fi in zip(elementos_x, frequencias))
    
    return soma_ponderada / n_total


def desvio_padrao(lista_de_dados_agrupados, media_valor):
    soma_di = 0
    soma_fi = 0
    
    for dados in lista_de_dados_agrupados:
        di = ((media_valor - dados["xi"]) ** 2) * dados["fi"]
        soma_di += di
        soma_fi += dados["fi"]
    
    if soma_fi == 0:
        return 0
    
    return math.sqrt(soma_di / soma_fi)


def coeficiente_variacao(desvio_padrao_valor, media_valor):
    if media_valor == 0:
        return 0
    
    return (desvio_padrao_valor / media_valor) * 100
