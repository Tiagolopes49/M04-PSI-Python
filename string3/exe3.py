#Tiago Lopes Nº28 10ºT

N=[]
n=int(input("Introduza quantos numeros pretende ter: "))
for i in range(n):
    n_lista=int(input("Introduza os numeros: "))
    N.append(n_lista)
print(N)
print(len(N))
media=sum(N)/len(N)
print(media)
maximo=max(N)
print(maximo)
N.sort(reverse=True)
print(n_lista)
if 5 in N:
    print("O numero 5 está na lista")
else:
    print("O numero 5 não está na lista")