from math import sqrt
opo = float(input('Digite o tamanho do cateto oposto'))
adj = float(input('Digite o tamanho do cateto adjacente'))
res = ((opo ** 2) + (adj ** 2))
res2 = (sqrt(res))
print('baseado nos tamanhos dos catetos que são {} e {} o tamanho da hipotenusa é {:.2f}'.format(opo, adj, res2))






