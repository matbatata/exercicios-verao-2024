n = int(input("digite um numero para saber se é primo: "))
i = 2

while i<=n:
    
    if i == n:
        print(n, "é primo")
    else:
        if n % i == 0:
            print(n, "não é primo")
            break
    i+=1


