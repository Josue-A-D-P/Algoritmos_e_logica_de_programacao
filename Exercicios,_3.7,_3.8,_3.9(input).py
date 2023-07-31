# Exercicio 3.7 soma dois numeros:

print('Exercicio 3.7\n')

N1 = int(input('Digite o primeiro numero: '))
N2 = int(input('Digite o segundo numero: '))

print(f'\nA soma de {N1} e {N2} é : {N1 + N2}')
print('\n=======================\n')

# Exercicio 3.8 converter metros em centimetros:

print('Exercicio 3.7\n')

metros = float(input('Digite a medida em metros: '))

centimetros = metros * 100

print(f'{metros} convertido em centimetros fica: {centimetros:.2f}')
print('\n=======================\n')

# Exercicio 3.9 converter para segungos:

print('Exercicio 3.7\n')

dias = float(input('Digite os dias: '))
horas = float(input('Digite as horas: '))
minutos = float(input('Digite os minutos: '))

segundos =  dias * 24 * 3600 + horas * 3600 + minutos * 60 
print(f'{dias} dias {horas} horas e {minutos} minutos fica:{segundos:10.2f} ')