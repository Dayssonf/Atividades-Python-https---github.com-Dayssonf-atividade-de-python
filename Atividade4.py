horas = int(input("Quantas horas o carro ficou? "))
preco_por_hora = 5

total = horas * preco_por_hora

if horas >5:
    total = total * 0.9

print(f"valor total: R$ {total}")
