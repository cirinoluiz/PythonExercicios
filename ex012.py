p = float(input('Qual o valor do produto?'))
d = (p - (0.05*p))
print('Parabéns! Você ganhou um desconto de 5%!\nO novo valor do seu produto é R${:.2f}'.format(d))
