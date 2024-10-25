serie = input("Digite ate qual serie deseja saber da sequencia de fibonacci: ")
while not serie.isnumeric():
    serie = input("Valor invalido. Por favor, tente novamente.\nDigite ate qual serie deseja saber da sequencia de fibonacci: ")
serie = int(serie)
i = 0
n1 = 0
n2 = 1
while i < serie:
    n3 = n1+n2
    n1 = n2
    n2 = n3
    i += 1
    print(n1, end=" ")
    