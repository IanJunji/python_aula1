i = 1
soma = 0
while i <= 5:
    num = input(f"Digite o {i}º número: ")
    if num.isnumeric():
        num = int(num)
        soma += num
        i += 1
    else:
        print("Valor inválido, por favor digite novamente.")
print(f"A soma dos 5 números é {soma} e a media é de {soma/5}.")

