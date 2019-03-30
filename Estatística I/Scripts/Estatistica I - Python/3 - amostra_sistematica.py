#importação das bibliotecas
import numpy as np
import pandas as pd
from math import ceil

#definição das variáveis
populacao = 150
amostra = 15

#divisão da população pela amostra - ceil arredonda para cima
k = ceil(populacao / amostra)

#sorteio para definir a variável de aleatoriedade entre 1 e k
r = np.random.randint(low = 1, high = k + 1, size = 1)

#definição de variável
acumulador = r[0]

#lista vazia para armezenar os valores sorteados
sorteados = []

#atribuir os valores na lista sorteados
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k

#carregamento do arquivo csv
base = pd.read_csv('1 - iris.csv')

#retornar o registros do arquivo csv de acordo com os índices sorteados
base_final = base.loc[sorteados]