contado = 0
numero = int(input("Digite um número: "))

while numero < 0:
    print("Número negativo! Digite novamente... ")
    numero = int(input("Digite um número: "))

contado += 1

print("quantidade de números digitados válidos:", contado)
    
