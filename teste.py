soma = 0
cont = 1 
while (cont <= 5):
	x = int(input(f'Digite o {cont} número:'))
	soma += x #equivalente: soma = soma + x
	cont += 1 #equivalente: cont = cont + 1 
print(f'Somatório: {soma}')