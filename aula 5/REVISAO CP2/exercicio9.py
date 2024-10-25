i = 0
pares = 0
impares = 0
while i < 10:
    i += 1
    num = input(f"Digite o {i}º número: ")
    while not num.isnumeric():
        num = input(f"Valor inválido. Por favor digite novamente.\nDigite o {i}º número: ")
    num = int(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Voce digitou {pares} números pares e {impares} números ímpares.")