'''
O sistema recebe a altura e a base de um triângulo e calcula sua área, com a ressalva de continuar
pedindo essas dimensões, caso, pelo menos uma delas for negativa ou 0.
'''

teste_base = True
teste_altura = True

while teste_base:

    base = float(input("Digite a base do triângulo: "))

    if base <= 0:
        print("Digite um valor positivo!")
    else:
        break

while teste_altura:

    altura = float(input("Digite a altura do triângulo: "))

    if altura <= 0:
        print("Digite um valor positivo!")
    else:
        break

print("A área do triângulo é", (base*altura)/2)