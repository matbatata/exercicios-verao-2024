salario = float(input("digite seu salario: ")) 
media = 1500
porcentagem = salario*(20/100)
if salario < 0:
    print("emprestimo negado")
elif salario>=media:
    print("emprestimo concedido")
elif salario<=media:
    print("emprestimo negado ")

# Nao precisava usar média... era para usar porcentagem.
