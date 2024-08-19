"""Подсчет элементов в словаре: Напишите программу, которая подсчитывает, сколько раз каждый элемент встречается в заданном массиве и выводит результат в виде словаря."""

def count_elements(arr):
    element_count = {}
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

input_arr = input("Введите числа массива через пробел: ")
numbers = list(map(int, input_arr.split()))

result = count_elements(numbers)
print("Количество каждого элемента:", result)
