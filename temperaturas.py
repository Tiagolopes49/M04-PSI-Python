#Tiago Lopes Nº28 10ªT

temperatura=[]
temp=input("Introduza as notas").split()
print(temp)
tempe=list(map(int,temperatura))
print(tempe)
soma=sum(tempe)
maximo=tempe.index(map(tempe))
minimo=tempe.index(min(tempe))
amplitude=maximo-minimo
print(amplitude)