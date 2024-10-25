num = input("Deseja saber a tabuada de qual número?\n-> ")
while not num.isnumeric():
    num = input("valor invalido, por favor tente novamente.\nDeseja saber a tabuada de qual número?\n-> ")
num = int(num)
i = 0
print(f"A tabuada do {num} é: ")
while i <= 10:
    tb = num*i
    i += 1
    print(tb, end=" ")