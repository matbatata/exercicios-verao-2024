v = float(input("Digite o valor das mercadorias: "))
print("1:MG")
print("2:SP")
print("3:RJ")
print("4:MS")
e = int(input("Escolha qual estado quer entregar: "))

mg = round(v*1.07,2)
sp = round(v*1.12,2)
rj = round(v*1.15,2)
ms = round(v*1.08,2)

if v < 0 and e < 0:
    print("Erro")
elif e == 1:
    print(mg)
elif e == 2:
    print(sp)
elif e == 3:
    print(rj)
elif e == 4:
    print(ms)

#corrigido
