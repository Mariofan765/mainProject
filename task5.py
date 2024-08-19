"""Объединение двух списков: Напишите функцию, которая объединяет два отсортированных массива в один отсортированный массив без использования дополнительной памяти."""

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

input_arr1 = input("Введите числа первого массива через пробел: ")
numbers1 = list(map(int, input_arr1.split()))
input_arr2 = input("Введите числа второго массива через пробел: ")
numbers2 = list(map(int, input_arr2.split()))

result = merge_sorted_arrays(numbers1, numbers2)
print("Объединённый отсортированный массив:", result)

