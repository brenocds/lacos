import random

num_jogadas = int(input("Quantas vezes você quer jogar a moeda? "))
num_caras = 0
num_coroas = 0

for i in range(num_jogadas):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        num_caras += 1
    else:
        print("Coroa")
        num_coroas += 1

print("Número total de caras:", num_caras)
print("Número total de coroas:", num_coroas)
