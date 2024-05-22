div = 1
contador = 1
x = int(input("Digite um número: "))
while contador <= x:
    contador+=1
    if x%div == 0:
        print(div)
    contador+=1
    div+=1        

"""
Falta o próprio número. Exemplo: quando x = 48, deveria imprimir:
1
2
3
4
6
8
12
16
24
48 
"""
