import math
media = 0
lst_dados = []

def media(lst_dados):
	soma = 0
	somafi= 0
	for i in lst_dados:
		soma += i["xi"] * i["fi"]
		somafi += i["fi"]
	return soma / somafi

def desvioPadrao(lst_dados):
	di = 0
	somaDi = 0
	somafi = 0
	for i in lst_dados:
		di = ((media - i["xi"]) ** 2) * i["fi"]
		somaDi += di
		somafi += i["fi"]
	return math.sqrt(somaDi / somafi)
	
def coeficienteVar(dp):
	return (dp / media) * 100

while True:
	xi = float(input("Digite o xi: "))
	fi = int(input("Digite o fi: "))
	
	dados = {"xi": xi, "fi":fi}
	
	lst_dados.append(dados)
	
	print(lst_dados)
	
	control = input("Deseja adicionar mais algum valor?")
	if control == "n":
		break

media = media(lst_dados)

dp = desvioPadrao(lst_dados)

cv = coeficienteVar(dp)

print(f"Desvio Padrão: {dp}\nCV: {cv}%")