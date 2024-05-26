def greet():
    print(f"""
Добро пожаловать
в игру
крестики-нолики
-----------------
Формат ввода: x y
x - номер строки
y - номер столбца""")

def show_field():
    """Создаём функцию для вывода поля"""
    print(f"""
   | 0 | 1 | 2 |
----------------""")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")
    print()

def ask():
    """Запрашиваем у пользователя данные, обрабатываем исключения"""
    while True:
        cords = input("Ваш ход: ").split() # считываем координаты

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

def check_win():
    """Определяем выигрышные комбинации, выводим информацию о победителе."""
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            show_field() # выводим последний ход перед объявлением победы
            print("Выиграл крестик!")
            return True

        if symbols == ["0", "0", "0"]:
            show_field() # выводим последний ход перед объявлением победы
            print("Выиграл нолик!")
            return True

    return False

greet()
field = [[" "] * 3 for i in range(3)] # создаём вложенные списки для определения полей в игре
num = 0

while True:
    num += 1
    show_field()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        break
        print("Ничья") # если кол-во ходов равно 9, объявляется ничья
