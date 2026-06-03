from funções.funcoes import coeficiente_variacao, desvio_padrao, media_agrupada

lst_dados = []


while True:
    xi = float(input("Digite o xi: "))
    fi = int(input("Digite o fi: "))

    dados = {"xi": xi, "fi": fi}

    lst_dados.append(dados)

    print(lst_dados)

    control = input("Deseja adicionar mais algum valor?")
    if control == "n":
        break

media_valor = media_agrupada([d["xi"] for d in lst_dados], [d["fi"] for d in lst_dados])

dp = desvio_padrao(lst_dados, media_valor)

cv = coeficiente_variacao(dp, media_valor)

print(f"Desvio Padrão: {dp}\nCV: {cv}%")
