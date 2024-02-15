#Tiago Lopes Nº28 10ºT

n_alunos=int(input("Introduza o números de alunos: "))
notas=input("Introduza as notas: ").split()
notas_alunos=list(map(int,notas))
media_minima=int(input("Introduza a media minima de aprovação: "))
print(notas_alunos)
media=sum(notas_alunos)/n_alunos
print(media)
aprovados=[]
for i in range(n_alunos):
    if notas_alunos[i]>media_minima:
        aprovados.append(i+1)
print(aprovados)
maximo=max(notas_alunos)
minimo=min(notas_alunos)
print(maximo)
print(minimo)
subtracao=maximo-minimo
print(subtracao)
if subtracao>50:
    print("Heterogénia")
else:
    print("Homogénia")