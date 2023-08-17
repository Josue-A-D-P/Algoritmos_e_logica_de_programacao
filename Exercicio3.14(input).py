# Exercicio 3.14 aluguel veiculo:

Km = float(input('Digite a quilometragem que você percorreu ou pretende percorrer com o veiculo: '))
dias = int(input('Digite quantos dias você ficou ou pretende ficar com o veiculo: '))

Valor_km = Km * 0.15
Valor_dias = dias * 60.00

tot = Valor_dias + Valor_km

print(f'O valor do aluguel fica em R$: {tot:.2f}')