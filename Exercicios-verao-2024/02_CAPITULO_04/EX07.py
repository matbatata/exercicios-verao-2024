v = float(input("Digite quantas mercaria quer transportar: "))
print("1:MG")
print("2:SP")
print("3:RJ")
print("4:MS")
e = int(input("Escolha qual estado quer entregar: "))
Minas = v*1.07
São_paulo = v*1.12
Rio_de_janeiro = v*1.15
Mato_grosso_sul = v*1.08
if v < 0 and e < 0:
    print("Erro")
elif e == 1:
    print(Minas)
elif e == 2:
    print(São_paulo)
elif e == 3:
    print(Rio_de_janeiro)
elif e == 4:
    print(Mato_grosso_sul)
