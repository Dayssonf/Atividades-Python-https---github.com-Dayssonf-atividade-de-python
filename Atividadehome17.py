while True:
    menu = int(input("Digite a opção: "))

    if menu == 1:
        print("Olá!")
    elif menu == 2:
        print("Tchau!")
    elif menu == 0:
        print("Sair!")
        break
    else:
        print("Opção Inválida! ")