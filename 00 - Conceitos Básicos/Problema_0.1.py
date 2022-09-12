'''
Para ser um circuito válido, ele precisa ter no mínimo 350 Km.
Sistema recebe o percurso e informa quantas vezes é necessário
percorrer para que ele tenha pelo menos a extensão mínima.
'''

from math import ceil

nome = input("Informe o nome do circuito: ")
km = float(input("Informe a extensão do circuito(km): "))

num_voltas = ceil(350 / km)
km_final = num_voltas * km

print("O circuito de", nome, "precisa de", num_voltas, "voltas para completar", km_final, "Km")