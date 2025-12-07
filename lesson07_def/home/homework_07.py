# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True: 
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

print("Task 1. Таблиця множення на задане число до максимального значення здобутку 25:")
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(num1, num2):
    return num1 + num2
num1 = 58777
num2 = 333
result = sum_numbers(num1, num2)
print(f"Task 2. Сума {num1} та {num2} становить: {result}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_numbers(list_num):
    return sum(list_num) / len(list_num)
list_num = [1, 2, 3, 50, 4]
print (f'Task 3. Середнє арифметичне списку чисел становить:', average_numbers(list_num))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_line(my_line):
    reverse_line = my_line[::-1]
    return reverse_line
my_line = "Будь-яка Абра-Абракадабра"
print(f'Task 4. Рядок у зворотньому порядку:', reverse_line(my_line))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest_word(words_list):
    longest_word = ""
    max_length = 0
    for word in words_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word
words_list = ['apple', 'banana', 'dog', 'vocabulary', 'link', 'key']
print(f'Task 5. Найдовше слово в списку:', the_longest_word(words_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.index(str2)
    else:
        index = -1
    return index

str1 = "Hello, world!"
str2 = "world"
print(f'Task 6. Індекс першого входження другого рядка у перший рядок, якщо другий рядок є підрядком першого рядка:', find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f'Task 6. Другий рядок не є підрядком першого рядка:', find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Урок 5, Вправа 3: Визначення високосного року
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")

def is_leap_year(my_year):
    if (my_year% 4 == 0 and my_year % 100 != 0) or (my_year % 400 == 0):
        print(f'Task 7. Визначення високосного року: {my_year} рік є високосним.')
    else:
        print(f'Task 7. Визначення високосного року: {my_year} рік не є високосним.')

my_year = int(input('Введіть рік для перевірки: '))
is_leap_year(my_year)

# task 8
# Урок 5, вправа 7: Зворотний порядок цифр
# print("Виведіть цифри числа у зворотному порядку")

def reverse_number(number):
    reverse_number = number[::-1]
    return reverse_number

number = input("Введіть число для виводу цифр в зворотньому порядку ")
print(f'Task 8. Ви ввели число {number}. Цифри числа в зворотньому порядку:', reverse_number(number))

# task 9
# Урок 5, вправа 9: Виключення зі списку
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

def exclude_items(fruits):
    print(f'Task 9. Список фруктів за виключенням "orange":')
    for fruit in fruits:
        if fruit == "orange":
            continue
        print(fruit)

fruits = ["apple", "banana", "orange", "grape", "mango"]
exclude_items(fruits)

# task 10
# Урок 3, вправа 17. Переведіть задачу з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі:
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?


def count_pages(all_fotos):
    page = int(8)
    count_pages = all_fotos / page
    return count_pages

all_fotos = int(input('Введіть кількість фотографій для прорахунку сторінок альбому: '))
print(f'Task 10. Щоб вклеїти {all_fotos} фотографій знадобиться', count_pages(all_fotos), 'сторінок')