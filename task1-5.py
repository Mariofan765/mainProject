def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Ввод данных
list1 = list(map(int, input("Введите элементы первого отсортированного списка через пробел: ").split()))
list2 = list(map(int, input("Введите элементы второго отсортированного списка через пробел: ").split()))

result = merge_sorted_lists(list1, list2)
print("Объединённый отсортированный список:", result)
