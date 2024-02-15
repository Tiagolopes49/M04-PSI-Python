#Tiago Lopes Nº28 10ºT

numero=[]

for i in range(1,6):
    n=int(input(f"Introduza o {i} valor: "))
    numero.append(n)
print(numero)
numero.sort()
print(numero)
numero.sort(reverse=True)
print(numero)