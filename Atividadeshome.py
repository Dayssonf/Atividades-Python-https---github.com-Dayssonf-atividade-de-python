idade = int(input("QUal a sua idade? "))

if idade < 0:
    print("Idade inválida! ")
elif idade >= 1 and idade <=12:
    print("Criança")
elif idade >=13 and idade <=17:
    print("Adolescente")
elif idade >=18 and idade <=59: 
    print("Adulto")
else:
    print("Idoso")