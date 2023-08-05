# Exercicio 3.10 calculo Aumento de salario:

print('Exercicio 3.10\n')

salario = float(input('Digite o salario: '))
aumento = float(input('Digite a porcentagem do almento: '))

novo_salario = salario * aumento / 100 + salario
aumento_salario = novo_salario - salario

print(f'O valor de almento é: {aumento_salario:.2f}')
print(f'E o novo salário fica: {novo_salario:.2f}')