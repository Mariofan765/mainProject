"""Поиск наибольшей невозрастающей подпоследовательности: Напишите функцию, которая находит наибольшую невозрастающую подпоследовательность в заданном массиве."""

def longest_non_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return []

    lnis = [1] * n
    prev_index = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] <= arr[j] and lnis[i] < lnis[j] + 1:
                lnis[i] = lnis[j] + 1
                prev_index[i] = j

    max_length = max(lnis)
    max_index = lnis.index(max_length)

    lnis_sequence = []
    while max_index != -1:
        lnis_sequence.append(arr[max_index])
        max_index = prev_index[max_index]

    return lnis_sequence[::-1]

input_arr = input("Введите числа массива через пробел: ")
numbers = list(map(int, input_arr.split()))

result = longest_non_increasing_subsequence(numbers)
print("Наибольшая невозрастающая подпоследовательность:", result)
