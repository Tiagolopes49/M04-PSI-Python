#Tiago Lopes Nº28 10ºT

idades=[]

idade=input("Introduza as idades").split()
print(idade)
idade1=list(map(int,idades))
print(idade1)
maximo=max(idades)
minimo=min(idades)
print(f"A idade mais baixa é:{maximo}")
print(f"A idade mais baixa é:{minimo}")
soma=sum(idade1)
print(soma)
media=sum(idade1)/len(idade1)
print(media)
idades.append(20)
print(idades)
idades.remove(17)
print(idades)
idades.pop(0)
print(idades)
idades.insert(0,12)
print(idades)