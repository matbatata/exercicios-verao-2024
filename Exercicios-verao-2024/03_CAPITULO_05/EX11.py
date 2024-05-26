x = int(input("Digite um número: "))
div = 1
contador = 1

while contador <= x:
    if x % div == 0:
        print(div)
    div += 1
    contador += 1

print(x)

#corrigido pelo mat
