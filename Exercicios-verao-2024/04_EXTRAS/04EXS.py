#variaveis
a = int(input("SUB 1 SOMA 2 escolha uma opção: "))
b = int(input("digite um numero: "))
c = int(input("digite mais um numero: "))

soma = a+b
sub = a-b


if a < 0: # intenção foi boa, mas eh bom usar o else aqui
    print("numero negativo")
elif a <= 1: # corrigir
    print(a-b)
elif a >= 2: # corrigir 
    print(b+c)

# Para pensar... e se na hora que eu colocasse o A, eu colocasse o numero 5 ou 7??
#O programa rodaria errado
