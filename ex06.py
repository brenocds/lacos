candidatos = {
    "Jair Rodrigues": 0,
    "Carlos Luz": 0,
    "Neves Rocha": 0,
    "Nulo": 0,
    "Branco": 0
}

def calcular_porcentagem(total_votos, votos):
    if total_votos == 0:
        return 0
    return votos / total_votos * 100

def determinar_vencedor(candidatos):
    vencedor = max(candidatos, key=candidatos.get)
    return vencedor

while True:
    print("As opcoes sao:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votacao")

    voto = input("Entre com o seu voto: ")

    if voto == "6":
        total_votos = sum(candidatos.values())
        total_nulos = candidatos["Nulo"]
        total_brancos = candidatos["Branco"]
        porcentagem_nulos = calcular_porcentagem(total_votos, total_nulos)
        porcentagem_brancos = calcular_porcentagem(total_votos, total_brancos)
        vencedor = determinar_vencedor(candidatos)

        print(f"Numero de votos para Jair Rodrigues: {candidatos['Jair Rodrigues']}")
        print(f"Numero de votos para Carlos Luz: {candidatos['Carlos Luz']}")
        print(f"Numero de votos para Neves Rocha: {candidatos['Neves Rocha']}")
        print(f"Numero de votos nulos: {total_nulos} ({porcentagem_nulos:.2f}%)")
        print(f"Numero de votos em branco: {total_brancos} ({porcentagem_brancos:.2f}%)")
        print(f"O candidato vencedor foi {vencedor}")
        break

    elif voto in ["1", "2", "3", "4", "5"]:
        candidatos[list(candidatos.keys())[int(voto)-1]] += 1

    else:
        print("Opcao invalida")
