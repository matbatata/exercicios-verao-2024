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

#corrigido pelo mat
