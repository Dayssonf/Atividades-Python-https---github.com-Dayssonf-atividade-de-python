while True:
    menu = int(input("Digite um número ente 1 a 10: "))

    if menu == -1:
        print("Sair!")
        break
    elif menu <0 or menu >10:
        print("Número inválido!")
    else: 
        break