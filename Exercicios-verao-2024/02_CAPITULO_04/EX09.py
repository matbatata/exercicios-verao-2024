altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

if altura <= 0 or peso <= 0:
    print("Dados inválidos")
elif altura <= 1.20 and peso <= 60:
    print("A")
elif 1.20 < altura <= 1.70 and peso <= 60:
    print("B")
elif altura > 1.70 and peso <= 60:
    print("C")
elif altura <= 1.20 and peso < 90:
    print("D")
elif 1.20 < altura <= 1.70 and peso < 90:
    print("E")
elif altura > 1.70 and peso < 90:
    print("F")
elif altura <= 1.20 and peso >= 90:
    print("G")
elif 1.20 < altura <= 1.70 and peso >= 90:
    print("H")
elif altura > 1.70 and peso >= 90:
    print("I")
else:
    print("Dado inválido")
#corrigido pelo mat
