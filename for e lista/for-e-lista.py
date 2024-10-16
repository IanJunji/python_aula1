'''vogal = 0
for char in "ian":
    if char in ['a','e','i','o','u']:
        vogal += 1
print(f"Há {vogal} vogais.")


for i in range(-10,11):
    print(i)

pares = 0
for i in range(10):
    if i % 2 == 0:
        pares += 1
print(pares)


tb = int(input("Número:"))
print(f"A tabuada do {tb} é:")
for i in range(11):
    mt = tb*i
    print(mt)
i = int(input("Número: "))
print(f"A tabuada do {i} é: ")
for j in range(1,11):
    print(f"{i}*{j} = {i*j}")

lista = [1, True, "ian", [], 3.8]
for elem in lista:
    print(elem)
    elem = 1
    print(elem)
print(lista)

profs = ['Lucioano', 'Yan', 'Danilo', 'Andre', 'Caio', 'Caio2']
for i in range(len(profs)):
    if profs[i] == "Danilo":
        print(f"O {profs[i]} está no índice {i}")

profs = ['Lucioano', 'Yan', 'Danilo', 'Andre', 'Caio', 'Caio2']
adj = ['maromba', 'foda', 'fortinho', 'maluco', '1', '2']
for i in range(len(profs)):
    print(f"O {profs[i]} é {adj[i]}")

valores = [50, 70, 1000000, 10, 20]
for i in valores:
    if i > maior:
        maior = i
print(maior)




valores = [50, 70, 1000000, 10, 20]
carros = ['up', 'kombi', 'celtinha brabo','gol','uno']
local_maior = 0
maior = valores[0]
for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        local_maior = i
print(f"O carro mais caro é o {carros[local_maior]} e custa {valores[local_maior]}")


lista = []
for i in range(10):
    lista.append(i)
    print(lista)
'''


def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

ano = checa_numero("Diga seu ano de nascimento: ")
qnt = checa_numero("Diga a qnt de garrafas: ")
