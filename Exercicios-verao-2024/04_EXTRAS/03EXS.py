peso = float(input("digite seu peso: "))

if peso<0:
    print("peso negativo")
elif peso<=80:
    print("peso normal")
elif peso>=80: # essa linha está errada
    print("acima do peso")
