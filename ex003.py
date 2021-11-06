n1 = int(input('Digite o primeiro número que deseja somar:'))
n2 = int(input('Digite o segundo número que deseja somar:'))
#O int, nas linhas anteriores, significa o tipo primitivo. No caso, int transforma a STRING em INTEIRO.
soma = n1+n2
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
#Se não houvesse "int" o print CONCATENARIA os objetos n1 e n2, pois seriam STRINGS.