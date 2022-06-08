cidade = input("Qual a sua cidade?")

cidade = cidade.split()

primeiro_nome = cidade[0]

if "santo" in primeiro_nome:
	print("tem santo")
else:
	print("nao tem santo")
