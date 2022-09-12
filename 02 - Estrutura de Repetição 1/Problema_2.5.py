'''
O sistema recebe 5 números inteiros e e mostre a soma dos números que são pares e a soma dos que são primos.
'''

def primo(n):
    divisores = 0
    contador = 1

    while contador <= n:

        if n % contador == 0:
            divisores += 1
        
        contador += 1

    if divisores <= 2:
        return True
    else:
        return False

x = 1
som_pares = som_primos = 0

while x <= 5:
    numero = int(input("Informe um número: "))
    
    if numero % 2 == 0:
        som_pares += numero
    
    if primo(numero):
        som_primos += numero
    
    x += 1

print("A soma dos números pares é:", som_pares, "\nA soma dos número primos é:",som_primos)