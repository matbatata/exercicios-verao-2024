nm1 = float(input("Digite massa do corpo 1 (kg): "))
pm1 = int(input("Digite a potência de dez associada a massa do corpo 1 (kg): "))

nm2 = float(input("Digite massa do corpo 2 (kg): "))
pm2 = int(input("Digite a potência de dez associada a massa do corpo 2 (kg): "))

nd = float(input("Digite a distância entre os corpos (m): "))
pd = int(input("Digite a potência de dez associada a distância entre os corpos: "))

ng = 6.6743
pg = -11

nr = round(nm1*nm2*ng/pow(nd,2),2)
pr = pm1+pm2+pg-pd*2

if nm1 <0 or nm2  < 0:
    print("Número inválido. Não existe massa negativa.")
else:
    print("A força gravitacional entre os corpos é: ", nr , "x10^", pr, "N", sep='')
