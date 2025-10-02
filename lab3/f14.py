import math
from itertools import permutations
import random

# 1. Граммы -> унции
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2. Фаренгейт -> Цельсий
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3. Объем сферы
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# 4. Уникальные элементы списка (без set)
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# 5. Палиндром
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 6. Обратный порядок слов в предложении
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

# 7. Перестановки строки
def print_permutations(s):
    perms = permutations(s)
    return ["".join(p) for p in perms]

# 8. Проверка простого числа
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 9. Фильтр простых чисел
def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]

# 10. Histogram
def histogram(lst):
    for num in lst:
        print("*" * num)

# 11. Задача "Угадай число"
def guess_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# 12. Проверка на "3 рядом с 3"
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# 13. Проверка на "007" в списке
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False
    return False


# ------------------------------
# Пример использования функций
# ------------------------------
if __name__ == "__main__":
    print("100 grams in ounces:", grams_to_ounces(100))
    print("Fahrenheit 100 to Celsius:", fahrenheit_to_celsius(100))
    print("Volume of sphere with radius 3:", sphere_volume(3))
    print("Unique list:", unique_list([1,2,2,3,4,4,5]))
    print("Is 'madam' palindrome?", is_palindrome("madam"))
    print("Reverse words:", reverse_words("We are ready"))
    print("Permutations of 'abc':", print_permutations("abc"))
    print("Filter primes:", filter_prime([1,2,3,4,5,6,7,11,13,15]))
    histogram([4, 9, 7])
    print("Has 33?", has_33([1,3,3]))
    print("Spy game:", spy_game([1,2,4,0,0,7,5]))
