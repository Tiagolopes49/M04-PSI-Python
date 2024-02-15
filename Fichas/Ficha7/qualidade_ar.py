#Tiago Lopes Nº28 10ºT

indice_poluicao=[]

for i in range(1,6):
    poluicao=int(input(f"Introduza o valor de {i} momento: "))
    indice_poluicao.append(poluicao)
somar=sum(indice_poluicao)
media=somar/len(indice_poluicao)
print(f"A média é {media:.2f}")

momentos_criticos=[]

for i in indice_poluicao:
    if i >100:
        momentos_criticos.append
if momentos_criticos:
    print(f"Os momentos criticos foram: {momentos_criticos}")
else:
    print("Não existem momentos criticos!")