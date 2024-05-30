i = 0
n = int(input("Digite um número: "))

while True:
    if n == 0:
        print("Erro")
    elif n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    i += 1
    break

print("O loop foi executado", i, "vezes.")

"""
1. O que era para esse código fazer? O código é pra fazer um loop de impar ou par
2. Sempre vai aparecer que o loop foi executado uma vez: vou consertar
3. Acredito que falta pedir em cada iteração do loop para o usuário digitar um número: a consertar
"""
