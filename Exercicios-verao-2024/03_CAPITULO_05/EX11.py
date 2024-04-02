i = 1
contador = 1
x = int(input("digite um número: "))
while contador <= x:
    contador+=1
    if x%i == 0:
        print(contador)
    contador+=1
    i+=1        