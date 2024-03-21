a = int(input("escolha uma opçao (GEO 1 PON 2 HAR 3 ARIT 4 SAIR 5) "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
d = int(input("digite um numero: "))
if a < 0 and a > 5:
    print("Saiu")
elif a == 1:
    print(b*c*d)
elif a == 2:
    print(b+2*c+3*d/6)
elif a == 3:
    print(1//1/b+1/c+1/d)
elif a == 4:
    print(b+c+d/3)
elif a == 5:
    print("SAIU")
