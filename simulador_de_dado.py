from random import randint

def pergunta_binaria(texto_pergunta):
	resposta = str(input(f"{texto_pergunta} [S/N] "))

	if resposta.upper() == "S":
		return True
	elif resposta.upper() == "N":
		return False
	else:
		print("Desculpe! Não consegui te entender. Tente de novo...")
		return pergunta_binaria(texto_pergunta)

def rodar_dado():
	return randint(1, 6)

jogando = pergunta_binaria("Gostaria de jogar o dado?")

while jogando:
	print(rodar_dado())
	jogando = pergunta_binaria("Gostaria de jogar o dado?")
