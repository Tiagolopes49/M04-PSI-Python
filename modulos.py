#Tiago Lopes Nº28 10ºT

notas=input("Introduza as notas(separadas por espaços): ").split()
print(notas)
PSI=list(map(int,notas))
print(PSI)
#alinia 1
soma=sum(PSI)
print(f"A soma das notas é: {soma}")
#alinia 2
media=sum(PSI)/len(PSI)
print(f"A media das notas é: {media:.2f}")
#alinea 3
maximo=PSI.index(max(PSI))+1
maior=max(PSI)
print(f"A nota mais alta é: {maior} no modulo {maximo}")
#alinia 4
minimo=PSI.index(min(PSI))+1
menor=min(PSI)
print(f"A nota mais baixa é: {menor} no modulo {minimo}")
#alinia 5
PSI[0]=14
print(PSI)
#alinia 6
contar=[1]*8
for i in range(0,7):
    if contar[i] !=0:
        for j in range(i+1, 8):
            if notas[i]==notas[j]:
                contar[i]+=1
                contar[j]=0
for i in range(0,8):
    if contar[i] !=0:
        print(f"{notas[i]} : {contar[i]}")
contar=PSI.count(14)
print(contar)