#Tiago Lopes Nº28 10ºT

cidades=["Viseu","Coimbra","Porto","Braga","Lisboa"]
c=input("Qual a cidade a substituir: ")
if c in cidades:
    indice=cidades.index(c)
    cidades[indice]="Lisboa"
    print(f"Lista atualizada: {cidades}")
else:
    print(f"A lista não foi atualizada")