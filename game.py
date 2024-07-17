from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError
# from inspect import isfunction, ismethod


game = Board()


def main():
    """Создать игровое поле - объект класса Board."""

    game = Board()
    current_player = 'X'
    running = True
    game.display()  # Отрисовать поле в терминале.

    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                # Пользователь воводит номер строки
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
                break

            except FieldIndexError:
                print('Неверный номер строки или столбца.')
                print('Значения должны быть неотрицательными или меньше '
                      f'{game.field_size}')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        game.make_move(row, column, current_player)
        # Перерисовать поле с учётом сделанного хода.
        game.display()
        if game.check_win(current_player):
            print(f'Победил {current_player}')
            running = False
        elif game.is_board_full():
            print('Ничья.')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
if __name__ == '__main__':
    main()
