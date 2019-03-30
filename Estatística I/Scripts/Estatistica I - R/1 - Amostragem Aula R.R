#Formacao Cientista de Dados - Fernando Amaral

#visualiza o conjunto de dados iris
iris

#tamanho do conjunto de dados
dim(iris)

#cria uma amostra - vamos gerar 150 números aleatórios 0s e 1s,
#com reposição obviamente com probabilidade de 50%
amostra = sample(c(0,1), 150, replace = TRUE, prob=c(0.5,0.5))

#exibe uma amostra
amostra

#tamanho da amostra com o elemento 0
length(amostra[amostra==0])

#tamanho da amostra com o elemento 1
length(amostra[amostra==1])

#grava o resultado da amostra
set.seed(2345)
sample(c(1000), 1)

#exibe o resumo do conjunto de dados iris
summary(iris)

#instalação de pacotes
install.packages("sampling")

#carregar o pacote
library("sampling")

#criação do extrato do conjunto de dados iris
amostrairis2=strata(iris,c("Species"),size=c(25,25,25), method="srswor")

#exibe o resumo da amostra amostrairis2
summary(amostrairis2)

#visualizar o conjunto de dados infert
infert

#verifica a base de dados
summary(infert)

#para gerar uma amostra com proporções iguais, no total de 100 elementos,
#devemos calcular: número de elementos do extrato dividido
#pela população total vezes o tamanho da amostra
#0-5: 12 / 248 * 100 = 5
#6-11: 120 / 248 * 100 = 48
#12+: 116 / 248 * 100 = 47

round(12 / 248 * 100)
round(120 / 248 * 100)
round(116 / 248 * 100)

#criação do extrato do conjunto de dados infert
amostra=strata(infert,c("education"),size=c(5,48,47), method="srswor")

#verifica a amostra
summary(amostra)

#chama a ajuda do método strata
help(strata)

#instala o pacote
install.packages("TeachingSampling")

#carregar o pacote
library("TeachingSampling")

#gerar uma amostra aleatória sistemática do conjunto de dados iris
#pega uma linha do conjunto a cada 10, no total da população de iris: 150
amostra = S.SY(150, 10)

#visualiza a amostra
amostra

#cria um subconjunto de dados amostrairis
amostrairis = iris[amostra,]

#visualiza a amostrairis
amostrairis

#tamanho da amostra iris
dim(amostrairis)