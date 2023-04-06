import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número secreto entre 1 e 100: "))
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")
