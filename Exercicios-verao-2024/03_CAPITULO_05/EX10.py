contador = 1 
soma = 0 

while contador <= 10:
    x = int(input("Insira um número: "))
    if x >= 0: 
        soma += x
        contador += 1
    else:
        print("insira um número positivo ou zero.")
media = soma / 10
print("A média é ", media)

#corrigido
