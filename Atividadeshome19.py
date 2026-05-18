lista = ("Carbonara", "Bolonhesa", "Parisiense" )
while True:
    menu = int(input("DIgita a opção: "))

    if menu ==1:
        print("Olá!")
    elif menu == 2:
        for i in range(len(lista)):
            print(f"{i + 1} - {lista[i]}")
    elif menu == 0:
        print("Sair!")
        break