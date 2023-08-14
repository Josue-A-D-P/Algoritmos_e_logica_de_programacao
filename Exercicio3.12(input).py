#Exercicio 3.12 calculo de tempo de viagem:

distancia = float(input('Digite a distância a percorrer: '))
velocidade = float(input('Digite a velocidade média da viagem: '))

tempo = distancia / velocidade
tempo_s = int(tempo * 3600) 
horas = int(tempo_s / 3600) 
tempo_s = int(tempo_s % 3600)
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
print("%02d Hora %02d minutos e %02d segundos" % (horas, minutos, segundos))