import random

print('''Please pick one:
            rock
            paper
            scissors''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: \n"))
#    player_b = str(input("Player b: \n"))
    a = game_dict.get(player_a)
    b = random.randrange(1,3,1)
    print(b)
    dif = a - b

    if dif in [-1,2]:
        print('player a wins')
        if str(input('Do you wanna to play another game? y/n:\n')).lower() == 'y':
            continue
        else:
            print('game over')
            break
    elif dif in [-2,1]:
        print('player b wins.')
        if str(input('Do you wanna to play another game? y/n:\n')).lower() == 'y':
            continue
        else:
            print('game over')
            break
    else:
        print('Draw')
        if str(input('Do you wanna to play another game? y/n:\n')).lower() == 'y':
            continue
