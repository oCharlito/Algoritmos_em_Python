import random

print('**')
print('Você é bom para adivinhar? ')
print('**')

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

print('Escolha um número entre 1 e 100 e tente adivinhá-lo!')
print('**')
print('Escolha o nível de dificuldade')
print('(1) Fácil  (2) Médio  (3) Difícil')
print('**')

nivel = int(input("Defina seu nível: "))
print('**')

if nivel == 1:
    total_tentativas = 15
elif nivel == 2:
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('Digite seu número: '))

    if chute < 1 or chute > 100:
        print('Por favor, digite apenas números entre 1 e 100')
        continue

    if chute == numero_secreto:
        print('Parabéns! Você acertou e fez {} pontos'.format(pontos))
        break
    else:
        if chute < numero_secreto:
            print('Lamento, você errou! Seu chute foi menor que o número secreto')
        else:
            print('Lamento, você errou! Seu chute foi maior que o número secreto')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print('O número secreto era:', numero_secreto)
