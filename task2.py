"""Проверка на палиндром: Напишите функцию, которая проверяет, является ли заданная строка палиндромом (читается одинаково слева направо и справа налево)."""

def is_palindrom(test_string):
    cleaned_string = ''.join(test_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

input_string = input("Введите текст для проверки: ")
result = is_palindrom(input_string)
print(result)