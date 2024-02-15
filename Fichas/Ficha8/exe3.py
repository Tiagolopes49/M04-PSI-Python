#Tiago Lopes Nº28 10ºT

def intercalarvetor(v1,v2):
    v3=[]
    n=len(v1)
    for i in range(n):
        v3.append(v1[i])
        v3.append(v2[n - i - 1])
    return v3

#programa principal

v1=[1,3,5,7]
v2=[2,4,6,8]
v3=intercalarvetor(v1,v2)
print(v3)