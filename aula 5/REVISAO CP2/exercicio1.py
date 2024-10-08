



nota = input("Digite uma nota de 0 a 10: ")
while True:
    if nota.isnumeric() and 10 > int(nota) > 0:
        print("Ótima escolha.")
        break
    else:
        print(f"O valor {nota} é inválido, por favor tente novamente.")
        nota = input("Digite um valor de 0 a 10: ")

