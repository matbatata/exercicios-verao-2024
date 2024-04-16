contador_positivo = 0
contador_negativo = 0
while True:
    x = int(input("Digite numeros inteiros: "))
    if x == 0:
        break
    elif x  < 0:
        print(x,"É negativo")
        contador_positivo+=1
    elif x > 0:
        print(x,"É positivo")
        contador_positivo+=1