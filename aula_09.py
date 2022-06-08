nome = input("Qual o seu nome?")

nome = nome.upper()

print(nome)

nome = nome.lower()

print(nome)

nome_lista = nome.split()
nome_lista = "".join(nome_lista)
print(len(nome_lista))

primeiro_nome = nome.split()
print(len(primeiro_nome[0]))