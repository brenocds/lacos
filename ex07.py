
p = float(input("Digite o valor inicial da sua aplicação: "))

i = 0.005

n = 12  

for mes in range(1, n+1):
    # calcula o montante
    m = p * (1 + i) ** mes
    # imprime o montante
    print(f"Mês {mes}: R${m:.2f}")

