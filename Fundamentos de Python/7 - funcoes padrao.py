#remove sinal
x = -10
print(abs(x))

#maior valor
z = [1, 1, 2, 3, 3, 3, 3, 4]
print(max(z))

#menor valor
print(min(z))

#arredondamento
t = 3.1417
print(round(t))

#soma os elementos
print(sum(z))

#importando biblioteca statistics
from statistics import *
print(mean(z))
print(median(z))
print(mode(z))
print(stdev(z))
print(variance(z))

#instalacao cmd python -m pip install numpy
from numpy import *
a = random.random((8,8))
print(a)