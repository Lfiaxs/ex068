from random import randint
print('-=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*20)
vitória = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitória += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitória += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('-'*20)
print(f'GAME OVER! Você venceu {vitória} vezes.')
