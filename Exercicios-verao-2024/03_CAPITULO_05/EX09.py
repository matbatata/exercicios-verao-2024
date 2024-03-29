contador = 1
maior = int(input("Digite um número: ")) 
while contador <= 9: 
    x = int(input("Digite um número: "))
    if maior < x:
        maior = x 
    contador+=1
print("O maior número e: ",maior)

# corrigido
