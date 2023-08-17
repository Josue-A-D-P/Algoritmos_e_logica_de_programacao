# Exercicio 3.15 Redução de vida:

C_dias = int(input('Em média quantos cigarros você fuma por dia: '))
tempo_f = int(input('A quantos anos você fuma: '))

tot_tempo = (C_dias * 10) * (tempo_f * 365)
tot_dias_perdidos = tot_tempo / (24 * 60)

print(f'Voce já perdeu em média {tot_dias_perdidos:.2f} dias de vida!!!')