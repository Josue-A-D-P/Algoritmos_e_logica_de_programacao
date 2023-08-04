# Exercicio 3.10 calculo Almento de salario:

print('Exercicio 3.10\n')

salario = float(input('Digite o salario: '))
almento = float(input('Digite a porcentagem do almento: '))

novo_salario = salario * almento / 100 + salario
almento_salario = novo_salario - salario

print(f'O valor de almento é: {almento_salario:.2f}')
print(f'E o novo salário fica: {novo_salario:.2f}')

print('\n======================\n')

# Exercicio 3.11 calculo de desconto mercadoria:

print('Exercicio 3.11\n')

V_mercadoria = float(input('Digite o valor da mercadoria: '))
P_desconto = float(input('Digite o percentual de desconto: '))

v_desconto = V_mercadoria * P_desconto / 100
novo_valor = v_desconto - V_mercadoria

print(f'O valor do desconto fica: {v_desconto:.2f}')
print(f'E a mercadoria fica por: { - novo_valor:.2f}')