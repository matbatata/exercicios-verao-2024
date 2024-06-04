print("Escolha seu gênero: ")
print("1.homem")
print("2.mulher")

p = int(input("Escolha uma opcão: "))

if p < 0 or p > 2:
  print("Erro: Opção inexistente")
else: 
    h = float(input("digite sua altura:  "))
    if h < 0:
        print("Erro: Altura negativa")
    else:
        homens = (72.7*h)-58
        mulheres = (62.1*h)-44.7
        if p == 1:
            print(round(homens,2))
        else:
            print(round(mulheres,2))
