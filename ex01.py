
valor_inicial = int(input("Digite o primeiro valor: "))
valor_final = int(input("Digite o último valor: "))

if valor_final > valor_inicial:
    tipo_contagem = "crescente"
else:
    tipo_contagem = "decrescente"

escolha = input("Digite 'w' para usar while ou 'f' para usar for: ")

if escolha == "w":
    contador = valor_inicial
    while contador <= valor_final if tipo_contagem == "crescente" else contador >= valor_final:
        print(contador)
        contador += 1 if tipo_contagem == "crescente" else -1
else:
    for contador in range(valor_inicial, valor_final + 1 if tipo_contagem == "crescente" else valor_final - 1, 1 if tipo_contagem == "crescente" else -1):
        print(contador)
