qn = int(input("Quantos números você deseja colocar? "))
if qn <= 0:
    print("Quantidade inválida(O codigo funciona com números positivos)")
else:
    mn = float(input("Digite o primeiro número: "))
    oc = 1
    contador = 1
    while contador < qn:
        n = int(input("Digite um número: "))
        if n > mn:
            mn = n
            oc = 1
        elif n == mn:
            oc+=1
        contador+=1
print(n)