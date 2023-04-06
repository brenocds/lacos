soma = 0
while True:
    num = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))
    if num < 0:
        break
    soma += num
print("A soma dos números digitados é:", soma)
