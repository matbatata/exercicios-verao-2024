div = 1
contador = 1
x = int(input("Digite um número: "))
while contador <= x:
    contador+=1
    if x%div == 0:
        print(div)
    contador+=1
    div+=1        
