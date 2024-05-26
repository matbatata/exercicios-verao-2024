n = int(input("Digite o número de linhas para o triângulo de Floyd: "))
linha = 1
num = 1

while linha <= n:
    coluna = 1
    while coluna <= linha:
        print(num)
        num += 1
        coluna += 1
    print()
    linha += 1

# está errado, a solução está no disc :D. Fizemos em aula
# mas valeu a tentativa. Prefiro que você erre tentando doq copiar a resposta sem pensar 
