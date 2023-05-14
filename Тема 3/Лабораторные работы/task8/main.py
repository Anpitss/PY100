money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение
value = 0
while value <= money_capital:
    money_capital = money_capital - spend + salary
    print(money_capital)
    value += 1
    month = value
    spend += spend * increase
print(month)
