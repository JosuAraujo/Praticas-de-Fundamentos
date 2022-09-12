'''
Sistema recebe o número e calcula seu fatorial. O Processo se repete até que
seja digitado um número negativo ou 0.
'''

def fatoracao(n):
    if n == 0:
        return 1
    else:
        return n * fatoracao(n-1)  

while True:
    n = int(input("Informe o valor deseja fatorar: "))

    if n > 0:
        print(fatoracao(n))
    else:
        break