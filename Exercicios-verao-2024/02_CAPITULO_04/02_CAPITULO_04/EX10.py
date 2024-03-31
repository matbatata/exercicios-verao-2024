print("1 - GEOMÉTRICA")
print("2 - PONDERADA")
print("3 - HARMÔNICA")
print("4 - ARITMÉTICA")

opcao = int(input("Insira a opção: "))

geometrica = pow(x*y*z, 1/3) # Esse daqui, eu forcei a barra. Foi mal
ponderada = (x + 2*y + 3*z)/6 
harmonica = 1/(1/x + 1/y + 1/z)
aritmetica = (x+y+z) / 3

# Observação
if opcao < 0 and opcao > 5:
    print("Saiu") # ok 

elif opcao == 1:
    # print(a*b*c) Você colocou a fórmula errada, mas valeu a intenção :)
    print(geometrica)

elif opcao == 2:
    #print(b+2*c+3*d/6) Nesta formúla, você esqueceu dos parênteses tomar cuidado...
    print(ponderada)

elif opcao == 3:
    #print(1//1/b+1/c+1/d) Esqueceu dos parênteses de novo...
    print(harmonica)
elif opcao == 4:
    #print(b+c+d/3) Precisava de parênteses... Quase certo! 
    print(aritmetica)
elif opcao == 5:
    print("SAIU") # essa linha não funciona... por quê? 

# parabéns!!
