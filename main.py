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

def mediana(lst_dados):
	mediana = 0
	fi_list = []
	for i in lst_dados:
		fi_list.extend([i["xi"]] * i["fi"])
	
	if len(fi_list) % 2 == 0:
		meio = len(fi_list) // 2

		dados_meio = fi_list[meio - 1: meio + 1]

		mediana = (dados_meio[0] + dados_meio[1]) / 2
	else:
		meio = fi_list[len(fi_list) // 2]
		mediana = meio
	
	return mediana



# def moda(lst_dados, media):
# 	fi_anterior = 0

# 	for i in lst_dados:
# 		delta1 = i["fi"] - fi_anterior
# 		i["fi"] + (delta1/ delta1)
# 		fi_anterior = i["fi"]



	

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

print(f"A médiana é: {mediana(lst_dados)}")