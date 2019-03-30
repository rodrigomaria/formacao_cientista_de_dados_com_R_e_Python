#vetores
lst = [1,2,3,4,5]
lst2 = [1,2,3,"4",True]
lst3 = [12,[1,2,3,4,5],"a"]
lst4 = list(range(0,10))

print(lst)

#acesso direto ao elemento de uma lista
lst[0]

#alterar diretamente o valor do elemento de uma lista
lst[0] = 12345

#numero de elementos de uma lista
len(lst)

#utilizando o comprimento da lista para imprimir
for n in range(0, len(lst4)):
    print(lst4[n])