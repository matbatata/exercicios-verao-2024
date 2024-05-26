n = int(input("Digite um número inteiro (ou um número negativo para parar: )"))

if n < 0:
    print("Nenhum número foi digitado.")
else:
    maior = n
    menor = n

    while True:
        n = int(input("Digite um número inteiro (ou um número negativo para parar): "))
        if n < 0:
            break
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    print("O maior número foi:", maior)
    print("O menor número foi:", menor)

#corrigido e aumentado pelo mat
