"""
i = 0
pares = 0
impares = 0
while i < 10:
    num = int(input(f"Diga o {i+1}° número: "))
    if num % 2 == 0:
        pares = pares + 1
    i = i + 1
print(f"Você digitou {pares} pares e {i - pares} ímpares.")


maxt = 0
senha = "1234"
tent = input("Digite sua senha: ")
while tent != senha and maxt < 5:
    #maxt = maxt + 1
    maxt += 1
    print("Acesso negado")
    tent = input("tente novamente")
if senha == tent:
    print("acesso liberado")
else:
    print("Tentativas esgotadas")


vinho1 = "Chapinha"
vinho2 = "Pérgola"
vinho3 = "Catuaba"
vinho = input("Qual vinho vc vai querer? \n->")
#while vinho != vinho1 and vinho != vinho2 and vinho != vinho3:
while not (vinho == vinho1 or vinho == vinho2 or vinho == vinho3):
    print("Esta não é uma opção")
    vinho = input("Digite novamente: ")
print("ótima escolha")

# Exercicio 1

numero = int(input("Digite um número: "))
while numero > 10 or numero < 0:
    print("Valor invalido")
    numero = int(input("Digite novamente\n->"))
print("Ótima escolha")


# Exercicio 2

nome = input("Digite seu nome")
while len(nome) < 3:
    print("nome invalido")
    nome = input("Digite novamente: ")
print("bela bosta")
idade = int(input("Agora digite sua idade: "))
while idade < 0 or idade > 150:
    print("valor invalido")
    idade = int(input("Digite novamente"))
salario =


# Exercicio 2 correcao

nome = input("Digite seu nome")
while len(nome) < 3:
    print("nome invalido")
    nome = input("Digite novamente: ")
while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade < 151 and idade > -1:
            break
        print("Valor invalido")
    else:
        print("Valor invalido")
while True:
    salario = input("Digite o seu salário: ")
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break
        print("Valor invalido")
    else:
        print("Valor invalido")
sexo = input("Qual o seu sexo?\n f: feminino\n m: masculino\n->")
while sexo != "f" and sexo != "m":
    print("Valor invalido")
    sexo = input("Digite novamente: ")
ec = input("Qual seu estado civil? \n s: solteiro(a) \n c: casado(a) \n v: viuvo(a) \n d: divorciado(a) \n ->")
while not (ec == "s" or ec == "c" or ec == "v" or ec == "d"):
    print("Valor invalido")
    ec = input("Digite novamente: ")



# Exercicio 3

popa = 80000
txa = 1.03
popb = 200000
txb = 1.015
i = 1
while popa <= popb:
    popa = popa * txa
    popb = popb * txb
    i += 1
print(i)



#Exercicio 4

i = 1
soma = 0
while i < 6:
    while True:
        n1 = input(f"Digite o {i}° número: ")
        if n1.isnumeric():
            n1 = int(n1)
            soma += n1
            i += 1
            break
        else:
            print("Valor invalido.")
media = soma/5
print(f"soma {soma} e media {media}")



# Exercicio 5

while True:
    n1 = input("Digite um número: ")
    if n1.isnumeric():
        n1 = int(n1)
        break
    else:
        print("valor invalido")
while True:
    n2 = input("Digite o segundo número: ")
    if n2.isnumeric():
        n2 = int(n2)
        break
    else:
        print("valor invalido")
menor = n1
if n2 < menor:
    menor = n2
maior = n1
if n2 > maior:
    maior = n2

while (menor + 1) < maior:
    menor = menor + 1
    print(menor)



# Exercicio 6

user = input("Digite seu novo nome de usuário.\n->")
senha = input("Digite sua nova senha.\n->")
while user == senha:
    print("O usuario e senha nao podem ser iguais.")
    user = input("Digite novamente seu nome de usuário.\n->")
    senha = input("Digite sua nova senha diferente do seu user.\n->")
print("Cadastro realizado.")



# Exercicio 7

while True:
    num = input("Digite o número que deseja saber a tabuada.\n-> ")
    if num.isnumeric():
        num = int(num)
        i = 0
        while i <= 10:
            tb = num * i
            i += 1
            print(tb)
        break



# Exercicio 8

n1 = 0
n2 = 1
fila = 0
while True:
    serie = input("Digite até qual serie da sequencia de fibonacci deseja saber. \n-> ")
    if serie.isnumeric():
        serie = int(serie)
        while fila <= serie:
            fila += 1
            aux = n2
            n2 = n2 + n1
            n1 = aux
            print(n1)
    else:
        print("Digite um valor valido, por favor")
    break


# Exerccicio 9

i = 0
pares = 0
while i < 10:
    i += 1
    num = int(input(f"Digite o {i}° número: "))
    if num % 2 == 0:
        pares = pares + 1
print(f"Tem {pares} pares e {10 - pares} ímpares.")


# Exercicio 10

while True:
    num = input("Digite o número que deseja descobrir seu fatorial: ")
    if num.isnumeric():
        num = int(num)
        aux = num - 1
        while aux > 0:
            num = num * aux
            aux = aux - 1
        print(num)
    else:
        print("Valor invalido, tente novamente")
    break



# Exercicio 11

n1 = 1
while True:
    n2 = input("Digite o número que deseja sabe se é primo ou não: ")
    if n2.isnumeric():
        n2 = int(n2)
        if n2 > 2:
            while n1 < n2-1:
                n1 += 1
                if n2 % n1 == 0:
                    print(f"O número {n2} não é primo.")
                    break
            else:
                print(f"O número {n2} é primo.")
        else:
            print(f"O número {n2} é primo.")
            break
    else:
        print("Valor invalido. tente novamente")
"""

# Exercicio 12

i = 0
soma = 0
while True:
    qnt_not = input("Deseja descobrir a media de quantas notas?\n->")
    if qnt_not.isnumeric():
        qnt_not = int(qnt_not)
        break
    else:
        print("Por favor insira um valor valido.")
while i < qnt_not:
    while True:
        i += 1
        nota = input(f"Digite a {i}ª nota: ")
        if nota.isnumeric():
            nota = int(nota)
            soma +=  nota
            break
        else:
            i -= 1
            print("Por favor insira um valor valido.")
media = soma/qnt_not
print(f"A media das {qnt_not} notas é {media}")