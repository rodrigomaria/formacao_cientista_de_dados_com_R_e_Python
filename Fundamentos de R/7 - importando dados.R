#importando dados csv
x = read.csv(file.choose(),header = TRUE,sep = ":")
x

#importando banco de dados
#Pacote RODBC
install.packages("RODBC")
library(RODBC)

conexao <- odbcDriverConnect('driver={SQL Server};server=DESKTOP-XXXXX\\SQLEXPRESS;database=VENDAS;trusted_connection=true')
resultado <- sqlQuery(conexao, "select * from dbo.vendas")
resultado
odbcClose(conexao)

#importando planilha do excel
#Pacote xlsx
install.packages("xlsx")
library(xlsx)
dados = read.xlsx(file.choose(),sheetIndex=1)
dados

#importando dados de outras ferramentas - Weka
#Pacote foreing
install.packages("foreing")
library(foreing)
dados = read.arff(file.choose())
dados