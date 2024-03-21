print("SUBTRAÇÃO - 1")
print("SOMA - 2")

# opcao
opcao = int(input("Escolha uma opção: "))

if opcao != 2 and opcao != 1:
    print("Número inválido")

else:
    #variáveis
    b = int(input("Digite um número: "))
    c = int(input("Digite mais um número: "))

    soma = b+c
    sub = b-c

    if opcao == 1: 
        print(sub)
    elif opcao == 2: 
        print(soma)
