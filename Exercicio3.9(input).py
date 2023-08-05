# Exercicio 3.9 converter para segungos:

print('Exercicio 3.7\n')

dias = float(input('Digite os dias: '))
horas = float(input('Digite as horas: '))
minutos = float(input('Digite os minutos: '))

segundos =  dias * 24 * 3600 + horas * 3600 + minutos * 60 
print(f'{dias} dias {horas} horas e {minutos} minutos fica:{segundos:10.2f} ')