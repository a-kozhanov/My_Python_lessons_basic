# coding=utf-8

__author__ = 'Ваши Ф.И.О.'

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('Введите возраст:')
age = input()
if int(age) >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
