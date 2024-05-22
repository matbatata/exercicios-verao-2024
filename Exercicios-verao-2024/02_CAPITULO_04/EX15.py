while True: 
    print("Calculando as raízes de uma equação de 2 grau")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))    
    c = float(input("Entre com o valor de c: "))
    
    delta = b**2 - 4*a*c  
    if delta >= 0:
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)

        print("Valor de x1:", x1)
        print("Valor de x2:", x2)
    else:
        print("Esta equação não possui raízes reais.")

#corrigido
