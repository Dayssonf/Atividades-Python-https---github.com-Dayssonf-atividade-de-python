def ler_alturas(): 
    alturas = [] #Uma lista é só uma caixa que guarda vários valores.
    quantidade = int(input("Quantas pessoas? "))

    for i in range(quantidade):
        altura = float(input(f"Digite a altura da pessoa {i +1}: "))
        alturas.append(altura) #append significa adicionar no final da lista.
    return alturas

lista = ler_alturas()
print(lista)

soma = 0

for numero in lista: 
    soma = soma + numero
print("Soma: ", soma)

media = soma / len(lista)
print("Média: ", media)

