#fruta
fruta=["banana","maça","pêras"]
print(len(fruta))
 
#ciclo for
for f in fruta:
    print(f)
 
#vou adicionar uma fruta
fruta.append("manga")
print(fruta)
 
#vai eliminar uma fruta especifica
fruta.pop(2)
print(fruta)
 
#vai eliminar um elemento
fruta.remove("banana")
print(fruta)
 
#vai ordenar os elementos
print("Ordenação")
fruta.sort()
print(fruta)
 
#vai ordenar de ordem decrescente
print("Ordenação na ordem decrescente")
fruta.sort(reserse=True)
print(fruta)