contador = 0

while True:
    numero = int(input("Digite a sua idade (-1 para sair): "))

    if numero == -1:
        break
    while numero <0: 
        print("Número inválido, digite novamente...")
        numero = int(input("Digite um número: "))

    contador += 1

    print(f"foram digitador {contador} validos. ")
    