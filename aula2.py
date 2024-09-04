"""
palavra = input("Diga uma palavra: ")
print(f"Você disse '{palavra}'")
print(type(palavra))
a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
print(f"A soma entre {a} e {b} é ")
# ----------------------------------
frase = "Eu"
print(frase)
frase = frase + " " + "Me"
print(frase)
frase = frase + " " + "chamo"
print(frase)
frase = frase + " " + "ian"
print(frase)
# -----------------------------------
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print(f"O resultado {a} > {b} é {a>b}")
print(f"O resultado {a} < {b} é {a<b}")
print(f"O resultado {a} == {b} é {a==b}")
print(f"O resultado {a} != {b} é {a!=b}")
print(f"O resultado {a} >= {b} é {a>=b}")
print(f"O resultado {a} < {b} é {a<=b}")
# -----------------------------------
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
# -------------------------------------------------------------------------------------------
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(f"O resultado de {a}>{b} and {a}<{b}, ou seja, {a > b} and {a < b} é {a > b and a < b}")
print(f"O resultado de {a}>{b} and {a}>={b}, ou seja, {a > b} and {a >= b} é {a > b and a >= b}")
print(f"O resultado de {a}<={b} and {a}=={b}, ou seja, {a <= b} and {a == b} é {a <= b and a == b}")
print(f"O resultado de {a}<{b} and {a}!={b}, ou seja, {a < b} and {a != b} é {a < b and a != b}")
# ------------------------------------------------------------------------------------------------
idade = int(input("Digite sua idade: "))
if idade > 17:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
# ----------------------------------------------------------------------------------------------
time = input("Para que time vc torce?\n->")
if time == "Corinthians":
    print("O maior do Brasil")
else:
    print("Chora mais")

"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número diferente do primeiro: "))
if n1 == n2:
    print("Os ")