import random
import  string
def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    str_pass = string.ascii_uppercase + string.ascii_lowercase + "0123456789"
    n = None
    if n is None:
        return ''.join(random.sample(str_pass, 8))
    else:
        return ''.join(random.sample(str_pass, n))


print(get_random_password())
