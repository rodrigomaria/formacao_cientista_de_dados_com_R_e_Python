#modulos
import statistics

z = [10,20,20,40]

x = statistics.mean(z)
y = statistics.median(z)

#usando alias nas importacoes
import statistics as est
x = est.mean(z)
y = est.median(z)

#importacao das funcoes diretamente
from statistics import mean, median
x = mean(z)
y = median(z)

#importacao de todas as funcoes do modulo
from statistics import *
x = mean(z)
y = median(z)

#instalando o pip no cmd: python -m ensurepip --default-pip
#instalando um pacote: python -m pip install numpy