def ler_numeros():
    numero = []

    quantidade = int(input("Quantos números você vai digitar? "))

    for i in range(quantidade):
        usuario = int(input(f"Digite o número do usuário {i + 1}: "))
        numero.append(usuario)
    return numero 

lista = ler_numeros()
print(lista)

soma = 0

for numero in lista:
    soma = soma + numero
print("Soma: ", soma)

media = soma / len(lista)
print("Média: ", media)