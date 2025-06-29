y = int(input("Введите год: "))


def is_year_leap(y):
    if y % 4 == 0:
        year_leap = True
        print("год ", y, ": ", year_leap, sep="")
    else:
        year_leap = False
        print("год ", y, ": ", year_leap, sep="")


is_year_leap(y)
