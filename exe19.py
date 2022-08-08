from random import choice
al1 = str(input('Primeiro aluno'))
al2 = str(input('Segundo aluno'))
al3 = str(input('Terceiro aluno'))
al4 = str(input('Quarto aluno'))
lista = [al1, al2, al3, al4]
sort = choice(lista)
print('Parabéns, o aluno vencedor do sorteio foi {}'.format(sort))










