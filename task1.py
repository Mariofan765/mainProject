"""Поиск наибольшего элемента: Напишите функцию, которая находит наибольший элемент в заданном массиве."""

def max_in_array(arr):
    print(max(arr))
    return(arr)

input_string = input("Введите числа через пробел: ")
numbers = list(map(int, input_string.split()))

max_in_array(numbers)