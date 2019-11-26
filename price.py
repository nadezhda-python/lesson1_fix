"""
price = 100
discout = 5

price_with_discount = price - price * discout / 100
print (price_with_discount)

def discounter(price, discout):
    if price > 0 and discout > 0 and discout < 100:
        print  (price - price * discout / 100)

discounter(100, 2)
"""
"""
Создайте функцию get_summ(one, two, delimiter='&'), 
которая принимает два параметра, приводит их к строке и отдает 
объединенными через разделитель delimiter
Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
положите результат в переменную и выведите ее значение на экран
Сделайте так, чтобы результирующая строка выводилась заглавными буквами


def get_summ(one, two, delimiter='&'):
    return str(one) + str(delimiter) + str(two)

res = get_summ('Learn', 'python')
print (res.upper())
"""

"""Создайте в редакторе файл price.py
Создайте функцию format_price, которая принимает один аргумент price
Приведите price к целому числу (тип int)
Верните строку "Цена: ЧИСЛО руб."
Вызовите функцию, передав на вход 56.24 и положите результат в переменную
Выведите значение переменной с результатом на экран"""

def format_price(price):
    try:
        int_price = str(int(price))
    except:
        return None
    return f'Цена: {int_price} руб.'

current_price = format_price('56.24')
print(current_price)