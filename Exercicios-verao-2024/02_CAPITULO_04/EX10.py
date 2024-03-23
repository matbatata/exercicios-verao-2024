# Eu prefiro que você coloque o nome da variável que seleciona uma opção como 'opcao', deixa mais claro
a = int(input("escolha uma opçao (GEO 1 PON 2 HAR 3 ARIT 4 SAIR 5) "))
# Apresente primeiro as opções, depois peça para o usuário escolher. Fica mais organizado
b = int(input("digite um numero: "))

c = int(input("digite um numero: "))
print("MÉDIA GEOMÉTRICA - DIGITE 1")
d = int(input("digite um numero: "))
print("MÉDIA PONDERADA - DIGITE 2")
if a < 0 and a > 5:
print("MÉDIA HARMÔNICA - DIGITE 3")
    print("Saiu")
print("MÉDIA ARITMÉTICA - DIGITE 4\n")
elif a == 1:

    print(b*c*d)
opcao = int(input("Escolha uma opção (1-4): "))
elif a == 2:

    print(b+2*c+3*d/6)
# Frases começam com letra maíuscula e número tem acento agudo
elif a == 3:
x = int(input("Digite um número: "))
    print(1//1/b+1/c+1/d)
y = int(input("Digite um número: "))
elif a == 4:
z = int(input("Digite um número: "))
    print(b+c+d/3)

elif a == 5:
# Apesar de colocar print(resposta) estar certo em alguns casos, eu prefiro que você crie variáveis 
    print("SAIU")
# Além disso, tente seguir o nome das variáveis do livro... É mais fácil para copiar :P

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
