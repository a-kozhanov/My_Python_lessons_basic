# coding=utf-8

__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

number = input('Введите произвольное число: ')

for x in range(len(number)):
    print(number[x])

print()

i = 0
while i < len(number):
    print(number[i])
    i += 1
