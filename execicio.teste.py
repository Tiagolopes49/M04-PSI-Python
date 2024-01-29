#Tiago Lopes Nº28 10ºT

numero=[]

for i in range(1,8):
    num=int(input(f"Introduza o {i} valor: "))
    numero.append(num)
soma=(sum(numero))
print(f"A soma é: ")
print(len(numero))
media=soma/len(numero)
print(f"A média é: ")

print(numero)
numero.sort()
print(numero)
numero.sort(reverse=True)
print(numero)

maior=max(numero)
print(f"O maior número é: ",maior)
menor=min(numero)
print(f"O menor número é:",menor)
maiorp=numero.index(max(numero))+1
menorp=numero.index(min(numero))+1
print(f"O maior número é:",maior)
print(f"O menor número é: ",menor)