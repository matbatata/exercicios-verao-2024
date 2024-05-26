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
#corrigido pelo mat(exercício dificil do caramba)
