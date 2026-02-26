km = int(input('Digite a distância em km: '))
dias = int(input('Digite a quantidade de dias: '))

preco_km = 0.15
preco_dia = 60
preco_total = km * preco_km + dias * preco_dia
print(f'A distância percorrida foi de {km} km e a quantidade de dias foi de {dias}.')
print(f'O preço total a ser pago é de R$ {preco_total}.')