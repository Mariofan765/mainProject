def are_anagrams(str1, str2):
    # Удаляем пробелы и приводим к нижнему регистру
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Сравниваем отсортированные версии строк
    return sorted(str1) == sorted(str2)

# Ввод данных
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if are_anagrams(string1, string2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
