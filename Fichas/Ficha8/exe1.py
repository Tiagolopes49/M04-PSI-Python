#Tiago Lopes Nº28 10ºT

notas=[]

for i in range(1,6):
    notas_turmas=int(input("Introduza as notas"))
    notas.append(notas_turmas)
maximo=max(notas)
menor=min(notas)
diferença=maximo-menor
print(f"A diferença entre a maior nota e a menor nota é: ",diferença)
if diferença>10:
    print(f"A turma é heterogénea")
else:
    print(f"A turmas não é heterogénea")
