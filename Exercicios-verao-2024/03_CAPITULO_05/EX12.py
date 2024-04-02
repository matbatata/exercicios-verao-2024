soma = 1
i = 1
contador = 0
x = int(input("Digite um número: "))
while contador <= x:
    contador+=1
    if x%i == 0:
        print(soma+contador)
    i+=1


    