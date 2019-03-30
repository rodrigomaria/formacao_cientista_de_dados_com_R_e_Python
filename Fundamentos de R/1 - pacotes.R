#instalacao de pacotes - só precisa instalar apenas uma vez em sua biblioteca
install.packages("e1071", dependencies = TRUE)

#carregar os pacotes sempre que precisar
library(e1071)

#descarregar o pacote
detach("package:e1071", unload = TRUE)