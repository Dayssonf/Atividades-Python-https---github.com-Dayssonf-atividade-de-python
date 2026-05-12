def ler_idades():
    idades = []

    quantidade = int(input("Quantas idades você vai digitar: "))
    for i in range(quantidade):
        usuario = int(input(f"Digite o número da sua idade {i + 1}: "))
        idades.append(usuario)
    return idades

lista = ler_idades()
print(lista)

soma = 0

for numero in lista:
    soma = soma + numero
print("Soma: ", soma)

media = soma / len(lista)
print("Média: ", media)

#idades = []       # várias coisas
#usuario = 28      # uma coisa só
#soma = 50         # conta
#media = 25.0      # resultado
