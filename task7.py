"""Переворачивание кортежа: Напишите функцию, которая переворачивает заданный кортеж."""

def reverse_cort(cort):
    print(cort[::-1])

input_cort = input("Введите данные для кортежа через запятую: ")
cort = tuple(input_cort.split(','))
cort = tuple(item.strip() for item in cort)

reverse_cort(cort)