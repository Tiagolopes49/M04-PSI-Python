#Tiago Lopes Nº28 10ºT
#transformar uma string em inteiro

PSI=[]
notas_PSI=input("Introduza as notas: ").split()
print(notas_PSI)

notas=list(map(int,notas_PSI))
print(notas)
media=sum(notas)/len(notas)
print(f"A média é:{media:.2f}")
maximo=notas.index(max(notas))+1
minimo=notas.index(min(notas))+1
print(f"A nota mais alta é:{maximo} e teve cotação maxima de {max(notas)}")
print(f"A nota mais baixa é:{minimo} e teve cotação minima de {min(notas)}")