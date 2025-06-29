m = int(input("Введите номер месяца: "))


def month_to_season(m):
    if (m > 2 and m < 6):
        print("Весна")
    elif (m > 5 and m < 9):
        print("Лето")
    elif (m > 8 and m < 12):
        print("Осень")
    elif (m == 12 or m == 1 or m == 2):
        print("Зима")
    else:
        print("Нет такого месяца в Григорианском календаре!")


month_to_season(m)
