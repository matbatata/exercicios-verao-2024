# Definindo as variáveis
n = int(input("Defina o enésimo termo: "))
contador = 1
i = 0
j = 1

if n <= 0:
    print("Número inválido")
elif n == 1:
    print(0)
elif n ==2:
    print(1)
else:
    while contador <= n-2:
        k = j+i
        i = j
        j = k
        contador+=1

    print("O valor da sequência de Fibonacci é:", k)
#corrigido em aula
