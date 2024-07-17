from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError
# from inspect import isfunction, ismethod


game = Board()


def save_result(results_game):
    """Сохранить результат игры - объект класса"""

    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(f'{results_game}\n')


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
            running = False
            result = f'Победил {current_player}!'
            save_result(result)
            print(result)
        elif game.is_board_full():
            running = False
            result = 'Ничья!'
            save_result(result)
            print(result)

        current_player = 'O' if current_player == 'X' else 'X'


# Всё, что ниже этой инструкции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
if __name__ == '__main__':
    main()
