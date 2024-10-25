def soma(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma
lista = [1,123,4,2,4,2,213,123,23,312]
soma_tot = soma(lista)
print(soma_tot)

