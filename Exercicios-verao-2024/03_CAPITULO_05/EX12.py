div = 1
contador = 1
soma = 0
x = int(input("Digite um número: "))
while contador <= x:
    contador+=1
    if x%div == 0:
        soma+=div
    contador+=1
    div+=1

print("Soma:", soma)

# corrigido
