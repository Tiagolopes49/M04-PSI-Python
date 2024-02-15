#Tiago Lopes Nº28 10ºT

nome=input("Introduza o seu nome completo: ")
parte=nome.split()
print(parte)
primeiro_nome=parte[0].capitalize()
ultimo_nome=parte[-1].capitalize()
print(primeiro_nome, ultimo_nome)
if "Cardoso" in parte:
    print("O teu nome tem Cardoso")
else:
    print("O teu nome não tem Cardoso")
