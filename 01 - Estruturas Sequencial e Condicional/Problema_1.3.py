'''
Sistema recebe um valor e retorna a forma que é possível converter esse valor dividindo ele em notas
de 100, 50, 20, 2 e 1 reis com o mínimo de cédulas possíveis. 
'''
from math import floor

dinheiro = int(input("Informe o valor (R$) que quer converter: "))
dinheiro_convertido = dinheiro

fator100 = fator50 = fator20 = fator2 = fator1 = 0

if dinheiro_convertido >= 100:
   fator100 = floor(dinheiro_convertido/100)
   dinheiro_convertido -= (100 * fator100)

if dinheiro_convertido >= 50:
   fator50 = floor(dinheiro_convertido/50)
   dinheiro_convertido -= (50 * fator50)

if dinheiro_convertido >= 20:
   fator20 = floor(dinheiro_convertido/20)
   dinheiro_convertido -= (20 * fator20)

if dinheiro_convertido >= 2:
   fator2 = floor(dinheiro_convertido/2)
   dinheiro_convertido -= (2 * fator2)

if dinheiro_convertido >= 1:
   fator1 = floor(dinheiro_convertido/1)
   dinheiro_convertido -= (1 * fator1)

print("Dinheiro =", dinheiro, "\n Nota R$100 =", fator100," \n Nota R$50 =", fator50,"\n Nota R$20 =", fator20,"\n Nota R$2 =", fator2," \n Moeda R$1 =", fator1)