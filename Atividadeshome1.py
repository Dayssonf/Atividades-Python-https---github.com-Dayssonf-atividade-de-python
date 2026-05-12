def main(): #cria a receita
    vendas = [] # Onde tudo vai ser Guardado

    while True: #Programa não fecha sozinho
        print("Menu")
        print("1 - Registrar venda")
        print("2 - Listar vendas")
        print("3 - Mostrar resumo")
        print("4 - sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "4": #única Saida
            print("Encerrando o programa...")
            break

main() #cozinha a receita