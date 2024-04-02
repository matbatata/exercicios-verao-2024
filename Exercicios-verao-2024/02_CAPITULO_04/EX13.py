a = int(input("Digite dois números: "))
b = int(input("Digite mais um: "))

print("1:SOMA")
print("2:SUB")
print("3:MULT")
print("4:DIV")

opcao = int(input("Escolha uma opção: "))

if opcao > 4 and opcao >= 0:
    print("ERRO")
elif opcao == 1:
    print(a+b)
elif opcao == 2:
    print(a-b)
elif opcao == 3:
    print(a*b)
elif opcao == 4:
    if b == 0:
        print("Não existe divisão por zero")
    else:
        print(a/b)

# corrigido
