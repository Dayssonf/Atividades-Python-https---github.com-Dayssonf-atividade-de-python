lista = []

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero == -1:
        print("Encerrando.")
        break
    else:
        lista.append(numero)

for numero in lista:
    print(numero)