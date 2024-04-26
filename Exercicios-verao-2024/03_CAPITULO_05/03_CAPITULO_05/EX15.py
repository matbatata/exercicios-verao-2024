numero = int(input("Digite um número inteiro (O comando para quando negativo): "))
maior = menor = numero
while numero >= 0:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    numero = int(input("Digite outro número inteiro (O comando para quando nagativo): "))
print("O maior número digitado é:", maior)
print("O menor número digitado é:", menor)