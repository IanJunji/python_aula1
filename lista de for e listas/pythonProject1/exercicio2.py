def num_maior(numeros):
    maior = 0
    for num in numeros:
        if num > maior:
            maior = num
    return maior


lista = [123,32,41,512123,2,4,8,1,3,5]
maior = num_maior(lista)
print(maior)

lista2 = [123,32,41,512123,2,4,8,1,3,12371837,5]
maior2 = num_maior(lista2)
print(maior2)

lista3 = [123,32,2131230192381,41,512123,2,4,8,1,3,12371837,5]
maior3 = num_maior(lista3)
print(maior3)