#Tiago Lopes Nº28 10ºT

temperatura_inicial=[]

for i in range(1,4):
    temperatura=int(input("Introduza a temperatura: "))
    temperatura_inicial.append(temperatura)
maximo=max(temperatura_inicial)
minimo=min(temperatura_inicial)
print(maximo)
print(minimo)