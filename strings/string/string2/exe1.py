#Tiago Lopes Nº28 10ºT


#1

nome=input("Introduza o nome completo: ")
print(nome)
print(nome[::-1])
print(len(nome)-nome.count(" "))
n=nome.split()
print(n)
print(len(n[0]))

#2
if ("Silva") or ("silva") in nome:
    print("esta")
else:
    print("não está")

#3
parte=nome.split()
print(parte)
primeiro_nome=parte[0].capitalize()
ultimo_nome=parte[-1].capitalize()
print(primeiro_nome, ultimo_nome)

#4
txt="Ontem já era tarde"
txt_alterado=txt.replace("a", " ").replace("A", " ").replace("á", " ")
print(txt_alterado)

#5
txt="ABABAAABABBAB"
c=txt.count("AB")
print(c)

#6
S1=input("Introduza uma primeira string: ")
print("O tamanho da primeira string é", len(S1))
S2=input("Introduza uma segunda string: ")
if S1==S2:
    print("São iguais")
else:
    print("São diferentes")
S3=S1+S2
print(S3)
print(S1[::-1])

c=input("Introduza o caracter a contar: ")
if c in S1:
    txt=S1.count
    print(f"O caracter {c} aparace {txt} na string")
else:
    print("O caracter não aparece na string")

#7
V1=[1,2,3,4]
V2=["a","b","c"]
V3=[]
tamanho=min(len(V1),len(V2))
for i in range(tamanho):
    V3.append(V1[i])
    V3.append(V2[i])

V3.extend(V1[tamanho:])
V3.extend(V2[tamanho])

#8
txt=input("Introduza uma frase: ")
espaços=txt.count(" ")
print(f"Na frase há {espaços} espaços em branco")

vogais="aeiou"
contagem_vogais=sum(1 for letra in txt if letra.lower() in vogais)
print(f"Na frase há {contagem_vogais} vogais.")

#9
def retorna_meses(valor):
    meses=[" ","janheiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    return meses[valor]

def converter_data(data):
    dia, mes, ano=data.split("/")
    valor=int(mes)
    print(f"Você nasceu a {dia} de {retorna_meses(valor)} em {ano}")

data=input("Introduza a data de nascimento (dd/mm/aaa):")
converter_data(data)

#10
n=int(input("Quantas temperaturs deseja inserir: "))
temp=[]
for i in range(1,n+1):
    t=float(input(f"Introduza a {i} temperatura: "))
    temp.append(t)
maxima=max(temp)
minima=min(temp)

amplitude=maxima-minima
print(amplitude)