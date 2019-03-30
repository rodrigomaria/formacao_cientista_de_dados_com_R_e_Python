#importacao das bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split

#carregamento do arquivo csv
iris = pd.read_csv('1 - iris.csv')

#contagem dos valores da coluna class
iris['class'].value_counts()

#iris.iloc - define as colunas que serão exibidas, começando em 0 e terminando na coluna 4 que não é exibida
#iris.iloc - o atributo que iremos fazer a divisão
#test_size - porcentagem da divisão da base de dados
#stratify - realizar o extrato dos registros, passando o campo que será extratificado
X, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size = 0.5, stratify = iris.iloc[:,4])

#contagem da quantidade de itens retornados na variável y
y.value_counts()

#carregamento do arquivo csv
infert = pd.read_csv('2 - infert.csv')

#contagem dos valores da coluna education
infert['education'].value_counts()

#amostra com 100 registros de infert
(120 / 248) * 100 #48
(116 / 248) * 100 #47
(12 / 248) * 100 #5

248 * 0.6 #148.79999999 (248 - 148 = 100 registros desejados), por isso test_size é 0.6

#infert.iloc - define as colunas que serão exibidas, começando em 2 e terminando na coluna 9 que não é exibida
#infert.iloc - o atributo que iremos fazer a divisão
#test_size - porcentagem da divisão da base de dados
#stratify - realizar o extrato dos registros, passando o campo que será extratificado
X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])

#contagem da quantidade de itens retornados na variável y1
y1.value_counts()