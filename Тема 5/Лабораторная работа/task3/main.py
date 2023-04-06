import random
def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = [random.randint(-10, 10)]
    while len(random_list) < 15:
        random_l = random.randint(-10, 10)
        if random_l not in random_list:
            random_list.append(random_l)
    return random_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
