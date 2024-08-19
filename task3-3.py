"""Поиск всех простых чисел в диапазоне: Напишите программу, которая находит все простые числа в заданном диапазоне и выводит их список."""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

prime_numbers = find_primes_in_range(start_range, end_range)
print("Простые числа в диапазоне:", prime_numbers)

