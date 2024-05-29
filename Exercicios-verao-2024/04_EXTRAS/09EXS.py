contador_positivo = 0
contador_negativo = 0

while True:
    x = int(input("Digite números inteiros: "))
    if x == 0:
        break
    elif x < 0:
        print(x, "é negativo")
        contador_negativo += 1
    elif x > 0:
        print(x, "é positivo")
        contador_positivo += 1

print("Total de números positivos:", contador_positivo)
print("Total de números negativos:", contador_negativo)

#corrigido pelo mat
