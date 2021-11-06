d = float(input('Quanto dinheiro você tem em sua carteira?'))
us = (d / 5.543304)  # valor do dólar no dia 06/11/2021
print('Você pode comprar US${:.2f} com R${:.2f}.'.format(us, d))
