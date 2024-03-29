altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
if altura <= 0 and peso <= 0:
    print("dados invalidos")
elif altura <= 1.20 and peso <= 60:
    print("A")
elif altura >= 1.20 or altura <= 1.70 and peso <= 60:
    print("B")
elif altura >= 1.70 and peso <= 60:
    print("C")
elif altura <= 1.20 and peso >= 60 or 90: # esse or 90 tá errado
    print("D")
elif altura >= 1.20 and peso >= 60 or 90:
    print("E")
elif altura >= 1.70 and peso >= 60 or 90:
    print("F")
elif altura <= 1.20 and peso >= 90:
    print("G")
elif altura >= 1.20 or altura <= 1.70 and peso >= 90:
    print("H")
elif altura >= 1.70 and peso >= 90:
    print("I")

# Eu tenho 1.74 e 75kg, eu deveria cair no F, mas cai no B.
