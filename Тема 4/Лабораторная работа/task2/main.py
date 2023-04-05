def get_count_char(str_):
    dict_ = {}
    str_low = str_.lower()
    for symbol_ in str_low:
        if symbol_.isalpha():
            if symbol_ in dict_:
                dict_[symbol_] += 1
            else:
                dict_[symbol_] = 1
    return dict_

def get_percent_char(dict_):
    sum_dict = 0
    for symbol_ in dict_:
        sum_dict += dict_[symbol_]
    for symbol_ in dict_:
        dict_[symbol_] = round(dict_[symbol_] / sum_dict * 100)
    return dict_




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percent_char(get_count_char(main_str)))