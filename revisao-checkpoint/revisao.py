# exercicio 1

n1 = int(input("Digite um número: "))
n2 = int(input("Agora digite outro número: "))
maior = n2
if n1 > n2:
    maior = n1
print(f"O maior número entre {n1} e {n2} é {maior}")

# exercicio 2

ano = int(input("Escreva o ano de seu nascimento:\n->"))
if ano < 2009:
    print("Você pode votar")
else:
    print("Você não pode votar")

# exercicio 3

senha = "1234"
tent = input("Digite a senha: ")
if tent == senha:
    print("Acesso permitido")
else:
    print("Acesso negado")

# exercicio 4

qnt = int(input("Quantas maçãs você quer?\n->"))
preco = 0.3
if qnt > 11:
    preco = 0.25
print(f"O total ficou R${qnt * preco}.")

# exercicio 5

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
meio = (n1+n2+n3) - (maior) - (menor)

print(f"a ordem crescente é: {menor, meio, maior}")

# exercicio 6

sexo = input("Qual o seu sexo?\n 1:feminino\n 2:masculino\n->")
altura = float(input("Agora digite sua altura em metros: "))
if sexo == 1:
    sexo = "feminino"
    pide = (62.1*altura)-44.7
else:
    sexo = "masculino"
    pide = (72.7*altura)-58
print(f"Sendo do sexo {sexo} e tendo {altura}m de altura. O seu peso ideal é {pide: .2f}Kg.")

# exercicio 7 e 8

lados = int(input("Quantos lados tem o seu polígono? \n->"))
if lados < 3:
    print("Nao é um polígono.")
elif lados == 3:
    md = float(input("Qual a medida dos lados do seu polígono? \n->"))
    area = ((md**2)*(3**(1/2))/2)
    print(f"Seu polígono é um Triângulo e tem uma área de {area: .2f}cm^2.")
elif lados == 4:
    md = float(input("Qual a medida dos lados do seu polígono? \n->"))
    area = (md**2)
    print(f"Seu polígono é um Quadrado e tem uma área de {area: .2f}cm^2.")
elif lados == 5:
    print(f"Seu polígono é um pentágono.")
else:
    print("Polígono não identificado.")

# exercicio 9

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f"O maior número é {maior}.")

# exercicio 10

md1 = int(input("Qual a medida do primeiro lado do seu triângulo?\n->"))
md2 = int(input("Qual a medida do segundo lado do seu triângulo?\n->"))
md3 = int(input("Qual a medida do terceiro lado do seu triângulo?\n->"))
if md1 == md2 == md3:
    tipo = "equilátero"
elif md1 != md2 != md3:
    tipo = "escaleno"
else:
    tipo = ("isósceles")
print(f"Seu triângulo é {tipo}.")

# exercicio 11

ang1 = int(input("Qual o valor do primeiro ângulo do seu triângulo?\n->"))
ang2 = int(input("Qual o valor do segundo ângulo do seu triângulo?\n->"))
ang3 = int(input("Qual o valor do terceiro ângulo do seu triângulo?\n->"))
if (ang1+ang2+ang3) != 180:
    print("Não corresponde à um triângulo.")
else:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        tipo = "retângulo"
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        tipo = "obtusângulo"
    else:
        tipo = "acutângulo"
    print(f"O seu triângulo é {tipo}.")