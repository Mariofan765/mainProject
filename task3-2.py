"""Удаление заданного элемента из массива: Напишите функцию, которая удаляет все вхождения заданного элемента из массива."""

def remove_element(arr, element):
    return [x for x in arr if x != element]

input_array = input("Введите числа через пробел: ")
numbers = list(map(int, input_array.split()))
input_num = int(input("Введите элемент для удаления: "))

result = remove_element(numbers, input_num)
print(result)
