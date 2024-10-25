num = input("Deseja saber o fatorial de qual número? \n-> ")
while not num.isnumeric():
    num = input("Valor invalido. Por favor digite novamente.\nDeseja saber o fatorial de qual número? \n-> ")
num = int(num)
i = num
while i > 1:
    i -= 1
    num *= i
print(num)