# importação das bibliotecas numpy e scipy-stats
import numpy as np
from scipy import stats

# cria um vetor de salários
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

# média
np.mean(jogadores)

# mediana
np.median(jogadores)

# quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])

# desvio padrao
np.std(jogadores, ddof = 1)

# resumo - quantidade de salarios no vetor, valor minimo e maximo, media, variancia
stats.describe(jogadores)