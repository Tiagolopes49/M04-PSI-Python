#Tiago Lopes Nº28 10ºT

caminhada=[]

for i in range(1,8):
    km=int(input("Introduza os km percorridos no {i} dia: "))
    caminhada.append(km)
soma=sum(caminhada)
print(soma)