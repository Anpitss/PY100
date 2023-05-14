list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_idx = 0
for i in range(len(list_numbers)):  # перебираем все индексы
    max_value = list_numbers[max_idx]
    current_value = list_numbers[i]
    if current_value > max_value:  # если текущее значение больше того, которое встречали ранее
        max_idx = i  # то перезаписываем индекс максимального значения

list_numbers[max_idx], list_numbers[-1] = list_numbers[-1], list_numbers[max_idx]   # меняем местами элементы
print(list_numbers)
