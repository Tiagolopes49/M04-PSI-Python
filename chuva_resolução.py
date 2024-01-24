#Tiago Lopes Nº28 10ºT
#Chuva

chuva=[] #lista vazia

for i in range(1,8): #7 dias
    q=int(input(f"Introduza a quantidade de chuva em mm que caiu no {i} dia da semana: "))
    chuva.append(q) #vai introduzir na lista/array os valores, um a um
soma=sum(chuva)
media=soma/len(chuva)
maior=chuva.index(max(chuva))+1 #posição da semana onde chuveu mais
menor=chuva.index(min(chuva))+1 #posoção da semana onde chuveu menos

print(f"A quantidade total de chuva durante a semana foi {soma} ")
print(f"A média de chuva foi {media:.2f}")
print(f"O dia com maior chuva foi {maior}")
print(f"O dia com menor quantidade de chuva foi {menor}")