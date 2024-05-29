while True:
    print("Opções:")
    print("1. Soma")
    print("2. Sub")
    print("3. Mult")
    print("4. Div")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 5:
        print("Saindo da calculadora")
        break
    elif escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:  
        x = int(input("Digite um número: "))
        z = int(input("Digite mais um número: "))
        if escolha == 1:
            print("Soma:", x + z)
        elif escolha == 2:
            print("Subtração:", x - z)
        elif escolha == 3:
            print("Multiplicação:", x * z)
        elif escolha == 4:
            if z != 0:  
                print("Divisão:", x / z)
            else:
                print("Erro: divisão por zero!")
    else:
        print("Escolha inválida")

#corrigido pelo mat
