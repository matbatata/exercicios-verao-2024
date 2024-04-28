n = int(input("Digite o número do termo da sequência de Fibonacci: "))

a, b = 0, 1
while n > 0:
    a, b = b, a + b
    n -= 1

print(n + 1, "termo da sequência de Fibonacci é:", a)