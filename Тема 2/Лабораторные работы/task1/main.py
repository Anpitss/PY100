list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
unique_numbers = set(list_)  # уникальные числа

sum_ = sum(unique_numbers)  # сумма уникальных чисел
print(sum_)

len_ = len(unique_numbers)  # количество уникальных чисел
print(len_)

average_ = round(sum_ / len_, 5)  # среднее арифметическое с округлением до 5  знаков
print(average_)

# TODO найти сумму, количество и среднее арифметическое уникальных чисел
