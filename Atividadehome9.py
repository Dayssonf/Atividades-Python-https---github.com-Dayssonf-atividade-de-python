numero = int(input("Digite um número: "))

if numero == 0:
    print("Número Inválido")

elif numero > 0 and numero % 2 == 0:
    print("Número positivo par ")

elif numero >0 and  numero % 2 == 1:
    print("Número positivo ímpar")

elif numero <0 and numero % 2 == 0:
    print("Número negativo par")

elif numero <0 and numero % 2 == 1:
    print("Número negativo Ímpar")
    