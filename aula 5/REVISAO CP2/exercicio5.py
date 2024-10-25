n1 = input("Digite um número: ")
while not n1.isnumeric():
    print("Valor inválido, por favor tente novamente.")
    n1 = input("Digite um número: ")
n1 = int(n1)
n2 = input("Digite outro número: ")
while not n2.isnumeric():
    print("Valor inválido, por favor tente novamente.")
    n2 = input("Digite outro número: ")
n2 = int(n2)
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = n1
print(f"Os números entre {n1} e {n2}, são: ")
while n1 < n2-1:
    n1 += 1
    print(n1, end=" ")
