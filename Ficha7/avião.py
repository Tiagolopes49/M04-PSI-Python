#Tiago Lopes Nº28 10ºT

aviao=[]

for i in range(1,11):
    nome=input("Introduza o seu nome: ")
    aviao.append(nome)
aviao.sort(reverse=True)
print(aviao)