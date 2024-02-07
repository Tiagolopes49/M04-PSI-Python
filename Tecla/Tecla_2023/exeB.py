#Tiago Lopes Nº28 10ºT
#o programa vai descobrir a idade da Mónica

idades = []
for i in range(3):
    idade = int(input(f"Introduza a idade da irmã {i+1}: "))
    idades.append(idade)
idades.sort()
idade_monica = idades[1]
print("A idade da Mónica é:", idade_monica)