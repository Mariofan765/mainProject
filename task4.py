"""Поиск пары с заданной суммой: Напишите функцию, которая находит все уникальные пары чисел в заданном массиве, сумма которых равна заданному числу."""

def sum_elem(arr, target):
    unique_pairs = set()
    seen = set()

    for number in arr:
        complement = target - number
        if complement in seen:
            unique_pairs.add((min(number, complement), max(number, complement)))
        seen.add(number)

    return list(unique_pairs)

input_string = input("Введите числа через пробел: ")
numbers = list(map(int, input_string.split()))
input_num = int(input("Введите число, которому должна быть равна сумма: "))

result = sum_elem(numbers, input_num)
print("Уникальные пары с заданной суммой:", result)
