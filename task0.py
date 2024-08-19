"""Сумма элементов массива: Напишите программу, которая вычисляет сумму всех элементов в заданном массиве."""

def sum_arr(a):
    total = sum(a)
    print(total)
    return total


input_string = input("Введите числа через пробел: ")
numbers = list(map(int, input_string.split()))


sum_arr(numbers)