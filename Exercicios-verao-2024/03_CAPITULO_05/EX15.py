n = int(input("Digite um número inteiro (para parar, insira um número negativo): "))
"""
Os números inteiros são: os positivos, ou negativos e o zero. Então, ao invés de (OU UM NÚMERO NEGATIVO ...),
eu preferi alterar para o que está está escrito. Fique atento aos conceitos

Link para leitura aprofundada:https://pt.wikipedia.org/wiki/N%C3%BAmero_inteiro
"""

if n < 0:
    print("Nenhum número foi digitado.")
else:
    maior = n
    menor = n

    while True:
        n = int(input("Digite um número inteiro (para parar, insira um número negativo): "))
        if n < 0:
            break
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    print("O maior número foi:", maior)
    print("O menor número foi:", menor)

#corrigido
# parabéns 
