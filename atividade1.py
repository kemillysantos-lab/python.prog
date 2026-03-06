m1 = float (input("Digite a nota do primeiro bimestre: "))
m2 = float (input("Digite a nota do segundo bimestre: "))
m3 = float (input("Digite a nota do terceiro bimestre: "))
media = (m1 + m2 + m3) / 3
if media >= 7:
    print(f'Parabéns! Você foi aprovado com média {media}.')
else: 
    print(f'Infelizmente, você foi reprovado com média {media}.')