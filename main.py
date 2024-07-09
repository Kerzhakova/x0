PURPLE = "\033[3;35m"
CYAN = "\033[3;36m"
LIGHT_RED = "\033[3;31m"
LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# код, который выводит  поле на экран
print(f'{CYAN}[{board[0]}] [{board[1]}] [{board[2]}]')
print(f'[{board[3]}] [{board[4]}] [{board[5]}]')
print(f'[{board[6]}] [{board[7]}] [{board[8]}]')

# чей ход
turn = 1 # номер хода
win = False
while not win:
    # проверяем, что мы достигли 10 хода
    if turn == 10:
        print('ничья')
        break
    if turn % 2 == 0:
        player = f'{PURPLE}o{CYAN}'
    else:
        player = f'{LIGHT_RED}x{CYAN}'
    answer = input(f'Куда поставить {player}? ')
    # метод isdigit() возвр. True если строка состоит из цифр
    if answer.isdigit():
        number = int(answer)
        # проверить что число не больше 9 и не меньше 1
        if 1 <= number <= 9:
            # проверить что клетка свободна
            if board[number - 1] == number:
                board[number - 1] = player
                # проверка победы
                for line in LINES:
                    i1 = line[0] # номер первой ячейки ЭТОЙ ЛИНИИ
                    i2 = line[1]
                    i3 = line[2]
                    if board[i1] == board[i2] == board[i3]:
                        print(f'{player} WIN')
                        win = True # останавливает цикл while
                        break # прерываем цикл for
                turn += 1       # передаем ход
            else:
                print('Клетка занята')
        else:
            print('Число должно быть от 1 до 9!!!!!!!!!!!!!!!!!')
    else:
        print('Нужно цифры')
    # вывожу доску
    print(f'[{board[0]}] [{board[1]}] [{board[2]}]')
    print(f'[{board[3]}] [{board[4]}] [{board[5]}]')
    print(f'[{board[6]}] [{board[7]}] [{board[8]}]')
