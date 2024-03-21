peso = float(input("digite seu peso: "))

if peso<0 and peso > 380:
    print("peso inválido")
elif peso<=80:
    print("peso normal")
elif peso>80: 
    print("acima do peso")