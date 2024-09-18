"""# exercicio 1

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


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
someios = (n1+n2+n3+n4) - maior - menor
if (n1 != maior) and (n1 != menor):
    meio1 = n1
elif (n2 != maior) and (n2 != menor):
    meio1 = n2
elif (n3 != maior) and (n3 != menor):
    meio1 = n3
elif (n4 != maior) and (n4 != menor):
    meio1 = n4
meio2 = someios - meio1
if meio1 > meio2:
    aux = meio1
    meio1 = meio2
    meio2 = aux
print(menor, meio1, meio2, maior)



# ---------------------------------------------------------------------------------------

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

someios = (n1+n2+n3+n4+n5) - maior - menor

if (n1 != maior) and (n1 != menor):
    meio1 = n1
elif (n2 != maior) and (n2 != menor):
    meio1 = n2
elif (n3 != maior) and (n3 != menor):
    meio1 = n3
elif (n4 != maior) and (n4 != menor):
    meio1 = n4
else:
    meio1 = n5

if (n1 != maior) and (n1 != menor) and (n1 != meio1):
    meio2 = n1
elif (n2 != maior) and (n2 != menor) and (n2 != meio1):
    meio2 = n2
elif (n3 != maior) and (n3 != menor) and (n3 != meio1):
    meio2 = n3
elif (n4 != maior) and (n4 != menor) and (n4 != meio1):
    meio2 = n4
else:
    meio2 = n5

meio3 = someios - meio1 - meio2

maior2 = meio1
if meio2 > maior2:
    maior2 = meio2
if meio3 > maior2:
    maior2 = meio3

menor2 = meio1
if meio2 < menor2:
    menor2 = meio2
if meio3 < menor2:
    menor2 = meio3
meiomeio = someios - maior2 - menor2



print(menor, menor2, meiomeio, maior2, maior)



num = int(input("Digite um número: "))
if num%2 == 0:
    print(f"{num} é par.")
else:
    print(f"{num} é ímpar.")


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
n6 = int(input("Digite o sexto número: "))
n7 = int(input("Digite o sétimo número: "))
n8 = int(input("Digite o oitavo número: "))
n9 = int(input("Digite o nono número: "))
n10 = int(input("Digite o décimo número: "))
if n1%2 == 0:
    m1 = " é par"
else:
    m1 = " é impar"
if n2%2 == 0:
    m2 = " é par"
else:
    m2 = " é impar"
if n3%2 == 0:
    m3 = " é par"
else:
    m3 = " é impar"
if n4%2 == 0:
    m4 = " é par"
else:
    m4 = " é impar"
if n5%2 == 0:
    m5 = " é par"
else:
    m5 = " é impar"
if n6%2 == 0:
    m6 = " é par"
else:
    m6 = " é impar"
if n7%2 == 0:
    m7 = " é par"
else:
    m7 = " é impar"
if n8%2 == 0:
    m8 = " é par"
else:
    m8 = " é impar"
if n9%2 == 0:
    m9 = " é par"
else:
    m9 = " é impar"
if n10%2 == 0:
    m10 = " é par"
else:
    m10 = " é impar"
print(f"{n1}{m1}, {n2}{m2}, {n3}{m3}, {n4}{m4}, {n5}{m5}, {n6}{m6}, {n7}{m7}, {n8}{m8}, {n9}{m9}, {n10}{m10}")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
n6 = int(input("Digite o sexto número: "))
n7 = int(input("Digite o sétimo número: "))
n8 = int(input("Digite o oitavo número: "))
n9 = int(input("Digite o nono número: "))
n10 = int(input("Digite o décimo número: "))
pares = 0
impares = 0
if n1%2 == 0:
    pares + 1
else:
    impares + 1
if n2%2 == 0:
    pares + 1
else:
    impares + 1
if n3%2 == 0:
    pares + 1
else:
    impares + 1
if n4%2 == 0:
    pares + 1
else:
    impares + 1
if n5%2 == 0:
    pares + 1
else:
    impares + 1
if n6%2 == 0:
    pares + 1
else:
    impares + 1
if n7%2 == 0:
    pares + 1
else:
    impares + 1
if n8%2 == 0:
    pares + 1
else:
    impares + 1
if n9%2 == 0:
    pares + 1
else:
    impares + 1
if n10%2 == 0:
    pares + 1
else:
    impares + 1
print(f"Existem {pares} números pares e {impares} números ímpares.")


pares = 0
impares = 0
i = 0
while i < 10:
    i = i + 1
    num = int(input(f"Diga o {i}° número: "))
    if num%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f"{pares} pares e {impares} ímpares.")


senha = "1234"
tent = input("Digite sua senha: ")
while tent != senha:
    print("Acesso negado")
    tent = input("Tente novamente: ")
print("Acesso permitido")



soma = 0
i = 0
while i < 10:
    n = int(input(f"Digite o {i+1}° número: "))
    soma = soma + n
    i = i + 1
print(f"A soma total é {soma}.")


soma = 0
i = 0
while i < 10:
    i = i + 1
    soma = soma + i
print(soma)
"""

