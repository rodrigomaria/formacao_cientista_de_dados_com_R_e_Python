#importacao de bibliotecas
import pandas as pd
import numpy as np

#carregamento do arquivo csv
base = pd.read_csv('1 - iris.csv')

#visualizacao dos dados no console
base

#visualizar a quantidade de linhas e colunas no console
base.shape

#gerar uma amostra com 0 e 1, populacao de 150, com reposicao, probabilidade de 50%
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])

#tamanho da amostra
len(amostra)

#tamanho da amostra com registros 0
len(amostra[amostra == 0])

#tamanho da amostra com registros 1
len(amostra[amostra == 1])

#sempre o mesmos dados da amostra
np.random.seed(2345)
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])