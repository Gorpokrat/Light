import math
def square(side):
    """Возвращает площадь квадрата, округленную вверх, если необходимо."""
    area = side * side
    return math.ceil(area)  # Округляем результат вверх
side_length = 4.5  
area_of_square = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area_of_square}")
