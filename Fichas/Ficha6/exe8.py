#Tiago Lopes Nº28 10ºT

numero=[]

for i in range(1,6):
    num=int(input(f"Introduza o {i} valor: "))
    numero.append(num)
soma=(sum(numero)) or numero.sum()
print(len(numero))
media=soma/len(numero)
print(media)