print("1 - GEOMÉTRICA")
print("2 - PONDERADA")
print("3 - HARMÔNICA")
print("4 - ARITMÉTICA")

opcao = int(input("Insira a opção: "))

x = float(input("Insira o valor de x: "))
y = float(input("Insira o valor de y: "))
z = float(input("Insira o valor de z: "))

geometrica = pow(x*y*z,1/3)
ponderada = (x+2*y+3*z)/6
harmonica = 1 / (1/x + 1/y + 1/z)
aritmetica = (x+y+z)/3

if opcao < 1 or opcao > 4:
    print("Opção inválida")
elif opcao == 1:
    print(geometrica)
elif opcao == 2:
    print(ponderada)
elif opcao == 3:
    print(harmonica)
elif opcao == 4:
    print(aritmetica)
#corrigido pelo mat
