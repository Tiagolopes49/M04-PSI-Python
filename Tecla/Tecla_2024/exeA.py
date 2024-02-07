#Tiago Lopes Nº28 10ºT

cabelos=[]

for i in range(1,6):
    cabelos_por_dia=int(input(f"Introduza os cabelos costados no {i} dia: "))
    cabelos.append(cabelos_por_dia)
print(cabelos)
dinheiro=sum(cabelos)*6
print(f"Ele ganhou dinheiro",dinheiro)