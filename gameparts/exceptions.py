class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'


class CellOccupiedError(Exception):

    def __str__(self) -> str:
        return 'Попытка изменить занятую ячейку'
