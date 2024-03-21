n = int(input("digite um numero: "))
resto = n % 2
i = 0
while i <= n:
    print(i)
    i+=1
if resto == 0:
    print("o numero é par!")
else:
    print("o numero é impar!")