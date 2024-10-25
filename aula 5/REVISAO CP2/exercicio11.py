num = input("Digite um número: ")
while not num.isnumeric():
    num = input("Valor invalido. Por favor digite novamente.\n Digite um número: ")
num = int(num)
i = 2
if num < 3:
    print(f"O número {num} é primo.")
else:
    while i <= num**(1/2):
        if num % i != 0:
            i += 1
        else:
            print(f"O número {num} não é primo.")
            break
    else:
        print(f"O numero {num} é primo.")