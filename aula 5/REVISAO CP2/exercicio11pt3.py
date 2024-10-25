nu = input('Digite um numero: ')
while not nu.isnumeric():
    nu = input('Valor invalido. Por favor tente novamente.\nDigite um numero: ')
nu = int(nu)
i = 2
while i <= nu**(1/2):
    if nu % i != 0:
        i += 1
    else:
        print(f'O numero {nu} não é primo')
        break
else:
    print(f'O numero {nu} é primo')
