while True:
    n = int(input("Digite um número: "))
    if n < 0:
        print("0 Não é divisor") # na verdade é, reescreva esta frase com uma verdade
        break
    if n % 5 == 0:
        print("O número",n,"é divisor de 5")
    else:
        print("o número",n,"não é divisor de 5")
    
