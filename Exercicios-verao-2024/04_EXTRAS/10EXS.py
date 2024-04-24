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
    elif escolha in ("1,2,3,4"): # Não ensinei isso...
        x = int(input("Digite um número: "))
        z = int(input("Digite mais um número: "))
    elif escolha == 1:
        print(x,"+",z = x+z)
    elif escolha == 2:
        print(x,"-",z = x+z)
    elif escolha == 3:
        print(x,"*",z = x*z)
    elif escolha == 4:
        print(x,"/",z = x/z)
        # falta um IF aqui... 
    else:
        print("Escolha invalida ")

    
