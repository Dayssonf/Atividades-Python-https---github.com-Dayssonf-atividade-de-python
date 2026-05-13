numeros = []
n1 = int(input("Digite o primeiro número: "))
numeros.append(n1)
n2 = int(input("Digite o segundo número: "))
numeros.append(n2)
n3 = int(input("Digite o terceiro número: "))
numeros.append(n3)

print(numeros)

soma = 0
for numero in numeros:
    soma = soma + numero     
print("soma: ", soma)

#“Comece a soma em zero. Para cada número que está dentro da lista numeros, some esse número ao total. No final, mostre a soma.”

media = soma/ len(numeros)
print("Média: ", media)