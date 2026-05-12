def listar_vendas(vendas):
    """Exibe todas as vendas registradas"""
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    print("\nVendas registradas:")
    for i, venda in enumerate(vendas, start=1):
        print(
            f"{i}. Produto: {venda['produto']} | "
            f"Qtd: {venda['quantidade']} | "
            f"Preço: R$ {venda['preco']:.2f} | "
            f"Total: R$ {venda['total']:.2f}"
        )


def registrar_venda(vendas):
    """Registra uma nova venda com validação"""
    produto = input("Nome do produto: ")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    while True:
        try:
            preco = float(input("Preço unitário: "))
            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número válido para o preço.")

    total = quantidade * preco

    venda = {
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco,
        "total": total
    }

    vendas.append(venda)
    print("Venda registrada com sucesso!")


def mostrar_resumo(vendas):
    """Mostra o resumo do dia"""
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    faturamento_total = sum(venda["total"] for venda in vendas)
    total_vendas = len(vendas)

    produtos = {}
    for venda in vendas:
        produto = venda["produto"]
        produtos[produto] = produtos.get(produto, 0) + venda["quantidade"]

    produto_mais_vendido = max(produtos, key=produtos.get)

    print("\nResumo do dia:")
    print(f"Total de vendas: {total_vendas}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Produto mais vendido: {produto_mais_vendido}")


def main():
    """Função principal do sistema"""
    vendas = []

    while True:
        print("\nMenu")
        print("1 - Registrar venda")
        print("2 - Listar vendas")
        print("3 - Mostrar resumo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_venda(vendas)

        elif opcao == "2":
            listar_vendas(vendas)

        elif opcao == "3":
            mostrar_resumo(vendas)

        elif opcao == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()