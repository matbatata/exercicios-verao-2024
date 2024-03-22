# Eu prefiro que você coloque o nome da variável que seleciona uma opção como 'opcao', deixa mais claro
# Apresente primeiro as opções, depois peça para o usuário escolher. Fica mais organizado

print("MÉDIA GEOMÉTRICA - DIGITE 1")
print("MÉDIA PONDERADA - DIGITE 2")
print("MÉDIA HARMÔNICA - DIGITE 3")
print("MÉDIA ARITMÉTICA - DIGITE 4\n")

opcao = int(input("Escolha uma opção (1-4): "))

# Frases começam com letra maíuscula e número tem acento agudo
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
z = int(input("Digite um número: "))

# Apesar de colocar print(resposta) estar certo em alguns casos, eu prefiro que você crie variáveis 
# Além disso, tente seguir o nome das variáveis do livro... É mais fácil para copiar :P

geometrica = pow(x*y*z, 1/3) 
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
