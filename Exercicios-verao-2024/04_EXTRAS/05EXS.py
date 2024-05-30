x = int(input("Digite um número: "))
potencia = 0

while potencia <= 5:
    # Calcula o dígito atual
    digito = (x // pow(10, potencia)) % 10
    print(digito)
    potencia += 1

# Se quiser imprimir o valor de potencia ao final do loop, faça isso fora do loop
print("Potência final:", potencia)
