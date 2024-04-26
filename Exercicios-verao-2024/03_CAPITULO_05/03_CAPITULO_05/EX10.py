contador = 1 
soma = 0 

while contador <= 10:
    x = int(input("Insira um número: "))
    soma += x
    contador+=1

media = soma / 10
print("A média é ", media)