n = int(input("digite um número: "))
i = 1

if n<0:
    print("não aceitamos numero negativo")
else:
    while i <= n:   
        print(i)
        i+=1
    print("Fim!")