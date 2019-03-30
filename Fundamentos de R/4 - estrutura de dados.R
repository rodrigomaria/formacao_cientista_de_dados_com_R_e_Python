#vetores - permite um unico tipo de dados
X <- 8

# c = combine
X <- c(1,2,3,4,5,6)
X
X[1]
X[1] <- 10
X[1]

Y <- c("a","b","c","d")
Y

Z <- c(1L,2L,3L)
Z


#matrizes - permite um unico tipo de dados
VADeaths
colnames(VADeaths)
rownames(VADeaths)

#so 1 coluna
VADeaths[,1]

#so 1 linha
VADeaths[1,]

#linhas 1 ate 3
VADeaths[1:3,]

#data frame - permite tipos de dados por coluna
longley

#funciona igualmente como em matrizes
longley[,1:3]

#acessar coluna com $
longley$Unemployed

#acessar coluna com nome
longley['Unemployed']

#listas com varios tipos de objetos diferentes
ability.cov

#acessando elementos
ability.cov$cov
ability.cov[1]

#verificando que sao objetos diferentes
class(ability.cov$cov)
class(ability.cov$center)

#acessando o elemento dentro de uma lista
ability.cov$cov[,1:3]

#fatores, variaveis categoricas com numero limitado de valores diferentes
#sao armazenados como inteiros
state.region