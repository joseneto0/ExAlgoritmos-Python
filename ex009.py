#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45
reais = float(input('Digite quantos reais você tem na carteira: '))
print(f'Convertendo sua carteira, você tem U$ {reais / 3.45:.2f}')