# if elif else
nota = 7
frequencia = 90

if nota >= 7 and frequencia > 70:
    print("Aprovado")
else:
    print("Reprovado")
    
if nota >= 7 or frequencia > 70:
    print("Aprovado")
else:
    print("Reprovado")
    
nota = 7
if nota <= 4:
    print("Reprovado")
elif nota > 4 and nota <= 6:
    print("Exame")
else:
    print("Aprovado")