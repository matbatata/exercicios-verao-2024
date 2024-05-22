while True:
    n = int(input("Digite um número inteiro (ou um número negativo para terminar): "))
    if n < 0:
        break
    elif n > maior:
            maior = n
    elif n < menor:
            menor = n
    print("O maior número é: ",maior)
    print("O menor número é: ",menor)

# Não funciona :(, você deve definir maior e menor antes de usá-los
