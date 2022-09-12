'''
Sistema  recebe um número inteiro positivo e indica se é primo ou não.
'''

n = int(input("Informe um número: "))

divisores = 0
contador = 1

while contador <= n:

    if n % contador == 0:
        divisores += 1
    
    contador += 1

if divisores <= 2:
    print("O número é primo.")

else:
    print("Não é primo")