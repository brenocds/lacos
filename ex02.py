while True:
    n = int(input("Digite um valor entre 1 e 10: "))
    if 1 <= n <= 10:
        break

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
