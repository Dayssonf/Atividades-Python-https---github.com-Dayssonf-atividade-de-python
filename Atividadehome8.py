n1 = float(input("Digite a primeira nota nota: "))
n2 = float(input("Digite a segunda nota nota: "))
n3 = float(input("Digite a sua frequência: "))
media = (n1 + n2) /2


if (n1 <0 or n1 >10) or (n2 <0 or n1 >10) or (n3 <0 or n3 >100):
    print("Dados Inválidos")

elif media >=7 and n3 >=75:
    print("Aluno Aprovado")

elif media >=4 and media <7 and n3 >=75:
    print("Aluno em recuperação")

else:
    print("Aluno reprovado")
    