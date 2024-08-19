"""Удаление дубликатов: Напишите программу, которая удаляет все дубликаты из заданного массива."""

def del_dupl(arr):
    ord_arr = list(set(arr))
    print(ord_arr)
    return ord_arr
    
input_string = input("Введите числа через пробел: ")
numbers = list(map(int, input_string.split()))
del_dupl(numbers)