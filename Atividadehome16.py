idade = int(input("Digite a sua idade: "))

while idade < 0 or idade >120:
    idade = int(input("Idade inválida. Tente novamente: "))

print("Idade Aceita!")