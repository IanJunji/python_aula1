num = input("Digite um numero: ")
while not num.isnumeric():
    num = input("Valor invalido. Por favor, digite um numero: ")
num = int(num)
i = 2
while i <= num**(1/2):
    if num % i != 0:
        i+=1
    else:
        print(f"{num} não é primo")
        break
else:
    print(f"{num} é primo")

