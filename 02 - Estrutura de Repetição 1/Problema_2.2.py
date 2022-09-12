'''
O código recebe o valor de uma viagem e a quantia inicial que vai ser depositada numa poupança, 
além de o valor que vai ser depositado por mês na mesma, e, assim, considerando o lucro de 0,5%
da poupança, indica quantos meses vão ser necessários para juntar a quantia.
'''

valor_viagem = float(input("Informe o valor da viagem: "))
valor_poup = float(input("Informe o valor que que há inicialmente na sua poupança: "))
valor_mes = float(input("Por fim, informe quanto você pretende depositar mensalmente a sua poupança: "))
meses = 0

while valor_poup < valor_viagem:

    valor_poup += (valor_poup * 0.005 + valor_mes)
    meses += 1  

print("Para conseguir o valor dessa viagem, você vai precisar de", meses, "meses.")