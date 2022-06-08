frase = str(input("digite uma frase: ")).strip()

print("a letra a aparece {} vezes na frase".format(frase.count("a")))


print("a posicao da primeira letra a: {}".format(frase.find("a")+1))
print("a posicao da ultima letra a: {}".format(frase.rfind("a")+1))