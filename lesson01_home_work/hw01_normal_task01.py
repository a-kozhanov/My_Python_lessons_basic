# coding=utf-8

__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


x = 58375

print('max_number = ', max(str(x)))

max_number = 0
for c in str(x):
    if int(c) > max_number:
        max_number = int(c)

print('max_number = ', max_number)

i = 0
while i < len(str(x)):
    if int(i) > max_number:
        max_number = int(i)
    i += 1

print('max_number = ', max_number)
