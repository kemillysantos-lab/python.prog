preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o desconto em porcentagem: (0 - 100%) '))

desconto = preco * percentual / 100
preco_final = preco - desconto

print(f'O preço do produto é {preco}. O desconto é {percentual}%.')
print(f'O valor calculado de desconto é {desconto}. O preço final do produto é {preco_final}')