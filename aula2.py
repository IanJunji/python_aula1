'''
palavra = input("Diga uma palavra: ")
print(f"Você disse '{palavra}'")
print(type(palavra))
a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
print(f"A soma entre {a} e {b} é ")
# ----------------------------------------------------------------------------------------------------------------------
frase = "Eu"
print(frase)
frase = frase + " " + "Me"
print(frase)
frase = frase + " " + "chamo"
print(frase)
frase = frase + " " + "ian"
print(frase)
# ----------------------------------------------------------------------------------------------------------------------
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print(f"O resultado {a} > {b} é {a>b}")
print(f"O resultado {a} < {b} é {a<b}")
print(f"O resultado {a} == {b} é {a==b}")
print(f"O resultado {a} != {b} é {a!=b}")
print(f"O resultado {a} >= {b} é {a>=b}")
print(f"O resultado {a} < {b} é {a<=b}")
# ----------------------------------------------------------------------------------------------------------------------
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(f"O resultado de {a}>{b} or {a}<{b}, ou seja, {a > b} or {a < b} é {a > b or a < b}")
print(f"O resultado de {a}=={b} or {a}!={b}, ou seja {a == b} or {a != b} é {a == b or a != b}")
print(f"O resultado de {a}>={b} or {a}!={b}, ou seja {a >= b} or {a != b} é {a >= b or a != b}")
print(f"O resultado de {a}<={b} or {a}>{b}, ou seja {a <= b} or {a > b} é {a <= b or a > b}")
print(f"O resultado de {a}!={b} or {a}<{b}, ou seja {a != b} or {a < b} é {a != b or a < b}")
print(f"O resultado de {a}>{b} or {a}>={b}, ou seja {a > b} or {a >= b} é {a > b or a >= b}")
print(f"O resultado de {a}<{b} or {a}=={b}, ou seja {a < b} or {a == b} é {a < b or a == b}")
print(f"O resultado de {a}=={b} or {a}>{b}, ou seja {a == b} or {a > b} é {a == b or a > b}")
# ----------------------------------------------------------------------------------------------------------------------
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(f"O resultado de {a}>{b} and {a}<{b}, ou seja, {a > b} and {a < b} é {a > b and a < b}")
print(f"O resultado de {a}>{b} and {a}>={b}, ou seja, {a > b} and {a >= b} é {a > b and a >= b}")
print(f"O resultado de {a}<={b} and {a}=={b}, ou seja, {a <= b} and {a == b} é {a <= b and a == b}")
print(f"O resultado de {a}<{b} and {a}!={b}, ou seja, {a < b} and {a != b} é {a < b and a != b}")
# ----------------------------------------------------------------------------------------------------------------------
idade = int(input("Digite sua idade: "))
if idade > 17:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
# ----------------------------------------------------------------------------------------------------------------------
time = input("Para que time vc torce?\n->")
if time == "Corinthians":
    print("O maior do Brasil")
else:
    print("Chora mais")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 1:

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número diferente do primeiro: "))
if n1 == n2:
    print("Os números são iguais, por favor digite números diferentes")
else:
    if n1 > n2:
        print(f"{n1} é o maior número")
    else:
        print(f"{n2} é o maior número")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 2:

ano = int(input("Digite o ano de seu nascimento: "))
if ano < 2009:
    print("Você pode votar")
else:
    print("Você não pode votar")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 3:

a = input("Digite sua senha de 4 dígitos:\n->")
if a == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 4:

a = int(input("As maçãs custam R$ 0,30 cada se forem compradas menos do que a dúzia, e R$ 0,25 se forem compradas pelo menos doze. Quantas maçãs você vai querer?\n->"))
if a < 12:
    pf = a * 0.30
    print(f"O total ficou R${pf}.")
else:
    pf = a * 0.25
    print(f"O total ficou R${pf}.")

# ......................................................................................................................
'''
# exercício 4 versao danilo

qnt = int(input("Digite quantas maçãs você vai querer: "))
preco = 0.3
if qnt >= 12:
    preco = 0.25
total = qnt*preco
print(f"O total ficou R${total}.")

# ----------------------------------------------------------------------------------------------------------------------
'''
# Exercício 5:

n1 = input("Digite o primeiro número: ") # 2
n2 = input("Digite o segundo número: ")  # 1
n3 = input("Digite o terceiro número: ") # 3
if n1 > n2:
    if n3 > n1:
        print(f"A ordem crescente dos números é: {n2}, {n1} e {n3}")
    elif n3 < n1:
        if n3 > n2:
            print(f"A ordem crescente dos números é: {n2}, {n3} e {n1}")
        else:
            print(f"A ordem crescente dos números é: {n3}, {n2} e {n1}")
else:
    if n3 > n2:
        print(f"A ordem crescente dos números é: {n1}, {n2} e {n3}")
    elif n3 < n2:
        if n3 > n1:
            print(f"A ordem crescente dos números é: {n1}, {n3} e {n2}")
        else:
            print(f"A ordem crescente dos números é: {n3}, {n1} e {n2}")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 6:

a = int(input("Digite qual o seu sexo. 1 para feminino e 2 para masculino\n->"))
if (a!=1) and (a!=2):
    print("Por favor, insira um valor válido.")
else:
    if a == 1:
        b = float(input("Agora digite sua altura em metros para descobrir o seu peso ideal:\n->"))
        pi = (62.1 * b) - 58
    else:
        b = float(input("Agora digite sua altura em metros para descobrir o seu peso ideal:\n->"))
        pi = (72.7 * b) - 44.7
    print(f"O peso ideal para a sua altura é: {pi: .2f}Kg.")



# Exercício extra:

l = input("Digite uma letra: ")
if (l=="a") or  (l=="e") or (l=="i") or (l=="o") or (l=="u"):
    print(f"A letra {l} é uma vogal")
else:
    print(f"A letra {l} é uma consoante.")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 7:

nl = int(input("Digite o número de lados do seu polígono regular\n->"))
if nl < 3:
    print(f"Não existe um polígono com apenas {nl} lados.")
elif nl < 4:
    md = int(input("Um polígono com 3 lados é um triângulo. Agora digite a medida (em cm) dos lados para descobrir a área do seu polígono.\n->"))
    a = float(((md**2)*(3**(1/2))/4))
    print(f"A área do seu triângulo é {a: .2f}")
elif nl < 5:
    md = int(input("Um polígono com 4 lados é um quadrado. Agora digite a medida (em cm) dos lados para descobrir a área do seu polígono\n->"))
    a = float(md**2)
    print(f"A área do seu quadrado é {a: .2f}")
elif nl < 6:
    print("Um polígono com 5 lados é um pentágono")
else:
    print("Polígono não identificado.")


# Exercício 8: complemento do ex 7 acima

# ----------------------------------------------------------------------------------------------------------------------

#Exercício 9:

print("Digite 3 números diferentes para descobrir qual é o maior entre os 3.")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if (n3==n2) or (n3==n1) or (n1==n2):
    print("Por favor, digite números diferentes.")
elif n1 > n2:
    if n3 > n1:
        print(f"O maior número entre:\n{n1}, {n2} e {n3}\nÉ o {n3}")
    else:
        print(f"O maior número entre:\n{n1}, {n2} e {n3}\nÉ o {n1}")
elif n2 > n1:
    if n3 > n2:
        print(f"O maior número entre:\n{n1}, {n2} e {n3}\nÉ o {n3}")
    else:
        print(f"O maior número entre:\n{n1}, {n2} e {n3}\nÉ o {n2}")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 10:

print("Digite as medidas do seu triângulo para saber se ele é Equilátero, Isósceles ou Escaleno:")
l1 = int(input("Digite a medida do primeiro lado: "))
l2 = int(input("Digite a medida do segundo lado: "))
l3 = int(input("Digite a medida do terceiro lado: "))
if l1==l2==l3:
    print(f"O triangulo de lados {l1}, {l2} e {l3} é equilátero.")
elif (l1==l2!=l3) or (l1!=l2==l3) or (l1==l3!=l2):
    print(f"O triangulo de lados {l1}, {l2} e {l3} é isósceles.")
else:
    print(f"O triangulo de lados {l1}, {l2} e {l3} é escaleno.")

# ----------------------------------------------------------------------------------------------------------------------

# Exercício 11:

print("Digite o grau dos ângulos internos do seu triângulo para saber se ele é reto, agudo ou obtuso:")
a1 = int(input("Digite o grau do primeiro ângulo do seu triângulo: "))
a2 = int(input("Digite o grau do segundo ângulo do seu triângulo: "))
a3 = int(input("Digite o grau do terceiro ângulo do seu triângulo: "))
if (a1+a2+a3) != 180:
    print("Por favor digite corretamente os ângulos do seu triângulo.")
elif (a1==90) or (a2==90) or (a3== 90):
    print(f"O triângulo de graus: {a1}, {a2} e {a3} é um triângulo retângulo.")
elif (a1>90) or (a2>90) or (a3>90):
    print(f"O triângulo de graus: {a1}, {a2} e {a3} é um triângulo obtusângulo.")
elif (a1<90) and (a2<90) and (a3<90):
    print(f"O triângulo de graus: {a1}, {a2} e {a3} é um triângulo acutângulo.")



'''
