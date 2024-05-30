import random
numero_secreto = random.randint(1,100)

while True:
    s = int(input("Descubra o número secreto: ")) 

    if s == numero_secreto: 
        break 
    elif s ==  numero_secreto+1 or s == numero_secreto-1: 
        print("Está perto")
    elif s > numero_secreto:
        print("Maior do que o número secreto")
    elif s < numero_secreto:
        print("Menor do que o número secreto")
    

print("O número secreto é: ",s)  
#corrigido
