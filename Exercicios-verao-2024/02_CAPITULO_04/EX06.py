p = int(input("Escolha uma opcão: "))
print("1.homem")
print("2.mulher")
h = float(input("digite sua altura:  "))
homens = (72.7*h)-58
mulheres = (62.1*h)-44.7
if h < 0 and p < 0 or p > 2:
  print("erro")
elif p == 1:
  print(homens)
elif p == 2:
  print(mulheres)

#arrumar tópicos abordados no discord
