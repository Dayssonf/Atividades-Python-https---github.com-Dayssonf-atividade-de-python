def ler_notas(): #Python, guarda esse código com o nome ler_notas
    notas = [] #Cria uma lista vazia

    quantidade = int(input("Quantas notas você vai digitar? ")) #Pergunta quantas vezes o for vai rodar

    for i in range(quantidade): #Repete o bloco várias vezes

        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    return notas #Quando terminar, devolve a lista pra quem chamou

notas = ler_notas()
print(notas)