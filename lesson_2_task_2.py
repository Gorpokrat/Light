def is_year_leap(year):
    return year % 4 == 0

# Выберите год для проверки
year_to_check = 2024 

# Вызов функции и сохранение результата
is_leap = is_year_leap(year_to_check)

# Вывод результата в консоль
print(f"Год {year_to_check}: {is_leap}")
