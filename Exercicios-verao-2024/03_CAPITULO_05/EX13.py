soma = 0
x = 1

while x <= 1000:
    if x % 3 == 0 or x % 5 == 0:
        soma += x
        print(x)
    x += 1

print("A soma é:", soma)

#corrigido
