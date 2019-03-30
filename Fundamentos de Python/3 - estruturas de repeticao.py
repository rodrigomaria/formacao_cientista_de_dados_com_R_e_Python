#while
count = 1
while count <= 5:
    print(count)
    count +=1
    
#for
for n in range(0,10):
    print(n)
    
for n in range(0,10):
    print(n+1)
    
for n in range(10,0,-1):
    print(n)
    
#range - valor de inicio, valor de parada e incremento opcional
range(0,10,1)
range(10,0,-1)

#break - cancela totalmente o laco
for n in range(0,10):
    if n == 4:
        break
    print(n)

#continue - reinicia o laco 
for n in range(0,10):
    if n == 4:
        continue
    print(n)