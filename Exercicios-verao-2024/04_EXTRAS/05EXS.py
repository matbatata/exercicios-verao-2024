x = int(input("Digite um número: "))
resto = 0
potencia = 0
while potencia <= 5:
    print(x // pow(10, potencia))
    potencia += 1
    if potencia == 2:
        print(potencia)
print(resto)

# o que era pra isso fazer?
