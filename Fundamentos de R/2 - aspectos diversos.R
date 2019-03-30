#localizar o diretorio padrao
getwd()

#alterar o diretorio padrao
setwd("c:\\data")

#encerrar o R
quit()

#descobrir o tipo do objeto
class(iris)

iristeste = iris

#salvando objetos - objetos devem ser declarados as variaveis
save(iristeste, file="iristeste.Rdata")

#limpa o objeto da memoria
rm(iristeste)

#visualiza o objeto
iristeste

#carregando objetos 
load(file="iristeste.Rdata")

#funcoes de visualizacao de dados
x = c(12,34,56,79)
y = c(1,6,9,14)

plot(x,y)
hist(x)
boxplot(x)