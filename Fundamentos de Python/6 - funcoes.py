#funcoes
def imprime():
    print("Esta é uma função!")
    
imprime()

#passando parametro
def imprimeN(n):
    print(n)
    
imprimeN("Impressão deste texto")

#funcao com retorno
def potencia(n):
    return n * n

x = potencia(5)
print(x)

#funcao com valores default
def intervalo(inic=1,fim=10):
    for inic in range(inic,fim+1):
        print(inic)
        
intervalo(5,25)
intervalo()