while True:
    n = int(input("Digite um número: "))
    if n < 0:
        print("0 Não é divisivel")
        break
    if n % 5 == 0:
        print("O número",n,"é divisor de 5")
    else:
        print("o número",n,"não é divisor de 5")

#corrigido pelo mat
