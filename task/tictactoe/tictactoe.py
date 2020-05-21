valid_chars = ['X', 'O', '_']
cells = [' '] * 9

winners = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

total_free = len([choice for choice in cells if choice in ' _'])

game_over = False
result = ''

valid_choice = False
current_player = 'X'

print('-' * 9)
print('| ' + ' '.join(cells[6:]) + ' |')
print('| ' + ' '.join(cells[3:6]) + ' |')
print('| ' + ' '.join(cells[:3]) + ' |')
print('-' * 9)

while not game_over:


    coords = input('Enter the coordinates: ').split()

    if not (coords[0].isdigit() and coords[1].isdigit()):
        print('You should enter numbers!')
        continue
    elif int(coords[0]) < 1 or int(coords[0]) > 3 or \
            int(coords[1]) < 1 or int(coords[1]) > 3:
        print('Coordinates should be from 1 to 3!')
        continue
    elif cells[(3 * (int(coords[1]) - 1)) + (int(coords[0]) - 1)] in 'XO':
        print('This cell is occupied! Choose another one!')
        continue
    else:
        cells[(3 * (int(coords[1]) - 1)) + (int(coords[0]) - 1)] = current_player
        valid_choice = True

        current_choices = [i for i in range(len(cells)) if cells[i] == current_player]

        for winner in winners:
            if len([cell for cell in current_choices if cell in winner]) == 3:
                game_over = True
                result = 'win'
                break
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        if result != 'win' and len([choice for choice in cells if choice in ' _']) == 0:
            game_over = True
            result = 'draw'

    print('-' * 9)
    print('| ' + ' '.join(cells[6:]) + ' |')
    print('| ' + ' '.join(cells[3:6]) + ' |')
    print('| ' + ' '.join(cells[:3]) + ' |')
    print('-' * 9)

if result == 'draw':
    print('Draw')
else:
    print('{0} wins'.format(current_player))
