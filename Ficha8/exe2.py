#Tiago Lopes Nº28 10ºT

carros=[]
somaimpar=0
somapares=0
for i in range(1,7):
    quantidade=int(input(f"Quantos carros entram na cidade no {i} dia: "))
    carros.append(quantidade)
    if (i%2==0):
        somapares=somapares+quantidade
    else:
        somaimpar+=quantidade

print(carros)
print("A soma dos números pares é",somapares)
print("A soma dos números impares é",somaimpar)

if somapares>somaimpar:
    print("Os dias pares devem ser fechados ao publico")
else:
    print("Os dias impares devem ser fechados ao publico")