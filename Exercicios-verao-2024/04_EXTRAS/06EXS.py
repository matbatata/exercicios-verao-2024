i = 0

while True:
    n = int(input("Digite um número (ou 0 para sair): "))
    
    if n == 0:
        print("Programa encerrado.")
        break
    
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    
    i += 1

print("O loop foi executado", i, "vezes.")

#Agora o código está certo
#Um código de impar ou par com loop
