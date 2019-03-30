#Formacao Cientista de Dados - Fernando Amaral

#criar a variável jogadores
jogadores = c(40000,18000,12000,250000,30000,140000,300000,40000,800000)

#exibir a variável jogadores
jogadores

#media
mean(jogadores)

#mediana
median(jogadores)

#exibir os quartis
quartis = quantile(jogadores)

#exibir a variável quartis
quartis

#exibir somente 75%
quartis[4]

#desvio padrao
sd(jogadores)

#resumo da variavel - minimo, primeiro quartil, segundo quartil, mediana, media, terceiro quartil, quarto quartil (max)
summary(jogadores)