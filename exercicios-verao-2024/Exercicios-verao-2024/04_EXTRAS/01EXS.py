ing = float(input("Digite a nota de Inglês: "))
mat = float(input("Digite a nota de Matemática: "))
por = float(input("Digite a nota de Português: "))

media = (ing+por+mat)/3
print ("A media foi: ", media)

if media >= 7:
    print ("aprovado")

else:
    print ("reprovado")

# parabéns 
# else não precisa de condição
