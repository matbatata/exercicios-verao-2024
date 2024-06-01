numero_de_linhas = int(input("Número de linhas é: "))
linha_atual = 1
cota = 0
elemento = 1

while linha_atual < numero_de_linhas:
    print(elemento, end=' ')
    elemento+=1
    cota+=1
    if linha_atual == cota:
        print()
        linha_atual+=1
        cota = 0

#feito em aula 
