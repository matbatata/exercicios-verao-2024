a = int(input("Digite dos numeros: "))
b = int(input("Digite mais um: "))
print("1:SOMA")
print("2:SUB")
print("3:MULT")
print("4:DIV")
c = int(input("Escolha uma opcao: "))
if c > 4 and c > 0:
    print("ERRO")
elif c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
