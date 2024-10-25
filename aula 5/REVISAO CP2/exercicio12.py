qnt = input("Deseja saber a media de quantas notas?\n-> ")
while not qnt.isnumeric():
    qnt = input("Valor invalido. Por favor, tente novamente.\nDeseja saber a media de quantas notas?\n-> ")
qnt = int(qnt)
i = 0
soma = 0
while i < qnt:
    i += 1
    nota = input(f"Digite a {i}º nota: ")
    while not nota.isnumeric():
        nota = input(f"Valora invalido. Por favor, tente novamente.\nDigite a {i}º nota: ")
    nota = int(nota)
    soma += nota
print(f"A media das {qnt} notas é {soma/qnt}")

