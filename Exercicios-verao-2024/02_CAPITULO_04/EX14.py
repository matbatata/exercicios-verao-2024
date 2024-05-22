numero = int(input("Digite um número: "))
if numero % 3 == 0 != numero % 5: # nem sabia que dava pra fazer isso... 
    print(numero, "é divisível por 3, mas não por 5")
elif numero % 5 == 0 != numero % 3:
    print(numero, "é divisível por 5, mas não por 3")
else:
    print(numero, "não é divisível por 3 ou 5, ou é divisível por ambos")
    
# Na linha 2, eu usaria numero % 5 == 0 and numero % 3 != 0:
# Na linha 4, eu usaria numero % 3 == 0 and numero % 5 != 0:

# corrigido
