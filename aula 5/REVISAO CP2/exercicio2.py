


nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Valor invalido, tente novamente.")
    nome = input("Digite seu nome: ")
idade = input("Qual a sua idade? \n->")
while not (idade.isnumeric() and 0 <= int(idade) <= 150):
    print("Valor invalido, por favor digite um número entre 0 e 150.")
    idade = input("Qual a sua idade? \n->")
salario = input("Qual o seu salário? \n->")
while not salario.isnumeric():
    print("Valor invalido, por favor digite novamente.")
    salario = input("Qual o seu salário? \n->")
sexo = input("Qual o seu sexo?\nf: feminino\nm: masculino\n->")

