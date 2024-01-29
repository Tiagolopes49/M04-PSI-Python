#Tiago Lopes Nº28 10ºT

prato_peixe=["peixe1","peixe2","peixe3","peixe4","peixe5"]
prato_carne=["carne1","carne2","carne3","carne4","carne5"]
ementa_10_dias=[]
for i in range(max(len(prato_carne))), len(prato_peixe):
    if i <len(prato_carne):
        ementa_10_dias.append(prato_carne[i])
    if i <len(prato_peixe):
        ementa_10_dias.append(prato_peixe[i])
    
for i in range(len(ementa_10_dias)):
    print("No () dia a ementa é {}".format(i+1, (ementa_10_dias[i])))