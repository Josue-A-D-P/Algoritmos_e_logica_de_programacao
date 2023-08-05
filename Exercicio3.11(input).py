# Exercicio 3.11 calculo de desconto mercadoria:

print('Exercicio 3.11\n')

V_mercadoria = float(input('Digite o valor da mercadoria: '))
P_desconto = float(input('Digite o percentual de desconto: '))

v_desconto = V_mercadoria * P_desconto / 100
novo_valor = v_desconto - V_mercadoria

print(f'O valor do desconto fica: {v_desconto:.2f}')
print(f'E a mercadoria fica por: { - novo_valor:.2f}')