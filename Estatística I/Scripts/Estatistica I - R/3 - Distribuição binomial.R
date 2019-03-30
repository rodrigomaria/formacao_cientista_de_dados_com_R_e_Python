#Formacao Cientista de Dados - Fernando Amaral

#calcular a probabilidade
#parametros: x - numero de sucessos, size - numero de experimentos, probabilidade
#jogar uma moeda 5 vezes e sair 3 caras
prob1 = dbinom(3,5,0.5)

#passar 4 sinais de 4 tempos cada, prob = 0, 1, 2, 3 e 4 sinais verdes
prob2 = dbinom(0,4,0.25)
prob3 = dbinom(1,4,0.25)
prob4 = dbinom(2,4,0.25)
prob5 = dbinom(3,4,0.25)
prob6 = dbinom(4,4,0.25)

#calcular a probabilidade cumulativa
#todas as probabilidades = 1
prob7 = pbinom(4,4,0.25)

#prova com 12 questões com 4 alternativas, chutar e acertar 7
prob8 = dbinom(7,12,0.25)