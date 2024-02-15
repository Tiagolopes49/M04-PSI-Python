#Tiago Lopes Nº28 10ºT

#exercicio sem clico for
km_por_dia=input("Introduza os km percorridos por dia: ").split()
km_dia=list(map(int,km_por_dia))
soma=sum(km_dia)
media=sum(km_dia)/len(km_dia)
print(soma)
print(media)
maximo=km_dia.index(max(km_dia))+1
print(maximo)

#exercicio com ciclo for
km=[]

for i in range(1,6):
    km_por_dia=int(input("Introduza os km percorridos por dia: "))
    km.append(km_por_dia)
print(km)
soma=sum(km)
media=sum(km)/len(km)
print(soma)
print(media)
maximo=km.index(max(km))+1
print(maximo)