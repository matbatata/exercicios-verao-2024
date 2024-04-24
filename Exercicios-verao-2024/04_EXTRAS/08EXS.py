import random
while True:
    s = int(input("Descubra o número secreto: "))
    x = random.randint(1,100)
    if s == 15:
        break 
    elif s > 15:
        print("Maior do que o número secreto")
    elif s < 15:
        print("Menor do que o número secreto")
    elif s == 14:
        print("Está perto")   
print("O número secreto é:",s)  

# Foi coirrigido no servidor... Rever e colocar o certo
