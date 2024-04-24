# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tqM-5OrjzI0ILzSBdWMa6H5SlFAws5qw
"""

#1.Write a Python program to calculate the length of a string.
def string_length(strin):
    count = 0
    for char in strin:
     count += 1
    return count
print(string_length(input()))

#2.Get a single string from two given strings, separated by a space and swap the first two characters of each string
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up(input(), input()))

#3.Write a Python program to lowercase the first n characters in a string.
n = input()
print(n[:5].lower() + n[5:])

# 4. Write a Python program to reverse a string
def reverse_string(str1):
    return ''.join(reversed(str1))
print(reverse_string(input()))

#5.Write a Python program to reverse words in a string.
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words(input()))

#6. Write a Python program to remove the n index character from a nonempty string.
def remove_char(str, n):
    first = str[:n]
    last = str[n+1:]
    return first + last
print(remove_char('MERITO', 0))
print(remove_char('MERITO', 3))
print(remove_char('MERITO', 5))

#  7.Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing', add 'ly' instead.
#  If the string length of the given string is less than 3, leave it unchanged.
def add_string(str1):

    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1
print(add_string('JA'))
print(add_string('one'))
print(add_string('runing'))

#8.Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def change_string(lan):
    return lan[-1:] + lan[1:-1] + lan[:1]
print(change_string('abcd'))
print(change_string('12345'))

#9.Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word, max_length

word_list =["jabłko", "banan", "pomarańcza", "kiwi", "truskawka"]
longest_word, length = find_longest_word(word_list)
print("Najdłuzsze słowo:", longest_word)
print("Dlugosc najgluzeszgo slowa:", length)

# 10.Write a Python program to sort a string lexicographically.
def lexicographic_sort(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string

string = "WSB-MERITO"
sorted_string = lexicographic_sort(string)
print("Posortowany ciąg:", sorted_string)

# 11. Write a Python program to display a number with a comma separator.
def numbers(number):
    formatted_number = format(number, ",")
    return formatted_number


number = 345000000
formatted_number = numbers(number)
print("Numer z przecinkami :", formatted_number)

# 12.Write a Python program to print the following numbers up to 2 decimal places.
def numbers():
    liczby = [3.14159, 2.71828, 9.87654321, 7.123456789]
    for liczba in liczby:
        print(f"{liczba:.2f}")
numbers()

#13. Write a Python program to find the first repeated character in a given string.
def repeat(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return char
        else:
            char_count[char] = 1
    return None

string = "Antonina"
first_repeated_char = repeat(string)
if first_repeated_char:
    print("Pierwszy powtarzający się znak to:", first_repeated_char)
else:
    print("W ciągu nie ma powtarzających się znaków.")

# 14.Write a Python program to remove spaces from a given string.
def remove_spaces(string):
    return string.replace(" ", "")

input_string = "Stduent na uczelni WSB"
output_string = remove_spaces(input_string)
print("Orginalny tekst :", input_string)
print("Tekst bez spacji ", output_string)

#15.Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index_characters(string):
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])

input_string = "witaj koelgo"
result_string = remove_odd_index_characters(input_string)
print("Orginalny tekst", input_string)
print("Tekst zmneiniony ", result_string)

# 16.Write a Python program to swap commas and dots in a string.
def swap(string):
    swapped_string = ""
    for char in string:
        if char == ',':
            swapped_string += '.'
        elif char == '.':
            swapped_string += ','
        else:
            swapped_string += char
    return swapped_string

input_string = "1345,232454.56"
swapped_string = swap(input_string)
print("Originalny tekst ", input_string)
print("Tekst po zmianie :", swapped_string)

#17.Write a Python program to compute the sum of the digits in a given string.
def sum(string):
    sumq = 0
    for char in string:
        if char.isdigit():
            sumq += int(char)
    return sumq

input_string = "abc124234233def45996"
result = sum(input_string)
print("Suma cyfr", result)

#18.Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
def prostokat(length, width):
    return length * width

def cylinder(radius, height):
    import math
    return math.pi * radius**2 * height

length = 3
width = 1
radius = 6
height = 42

area = prostokat(length, width)
volume = cylinder(radius, height)

print("Pole prostokąta:", area, )
print("Objętość walca:", volume, )

#19.Write a Python function to create an HTML string with tags around the word(s).
def wrap_with_html(text, tag):
    return f"<{tag}>{text}</{tag}>"
word = "To jest przykładowy tekst"
tag = "strong"
html_string = wrap_with_html(word, tag)
print(html_string)

#20.Write a Python program to count and display vowels in text.
def count_and_display_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    vowel_list = []

    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    print("Liczba samogłosek:", vowel_count)
    print("Samogłoski w tekście:", ', '.join(vowel_list))

input_text = "Siemnako "
count_and_display_vowels(input_text)