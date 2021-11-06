a = float(input('Qual a altura da parede?'))
la = float(input('Qual a largura da parede?'))
mq = (a * la)  # calcula os metros quadrados da parede.
t = 2  # quantidade de metros quadrados que cada litro de tinta pinta é 2m quadrados
qt = (mq / t)
print('A quantidade necessária de litros de tinta é: {} Litros'.format(qt))
