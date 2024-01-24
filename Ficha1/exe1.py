import numpy as np
array_par=np.array([2,4,6,8,10])  #criar o array
print(array_par)

print(type(array_par))            #tipo de dados
dimensao=array_par.shape
print(dimensao)

print(array_par+5)                #adiciona 5 a todos os valores do array

print(array_par*3)                #multiplica por 3 todos os elementos array

array_impar=np.array([1,3,5,7,9]) #cria um novo array com os elementos [1,3,5,7,9]

print(array_par+array_impar)      #soma os dois arrays elemento a elemento 

print(array_par-array_impar)      #calcula a diferença  entre o primeiro e o segundo array

print(array_par[2])               #extrai o elemento 2

print(array_impar[1:4])           #conten os elementos do indice 1 e 3

media=np.mean(array_par)          #calcula a média dos elementos do primeiro array
print(media)

max=np.max(array_impar)           #encontra o valor máximo do segundo array
print(max)