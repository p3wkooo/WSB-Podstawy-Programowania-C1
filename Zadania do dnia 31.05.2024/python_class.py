# -*- coding: utf-8 -*-
"""Kopia notatnika Python Class.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jgmvwyciRKRKYkZpfMFimWJ9yp0pmKHf
"""

#Python class, Basic exercises

#1. Write a Python program to import a built-in array module and display the namespace of the said module.
import array
print(dir(array))

#2. Write a Python program to create a class and display the namespace of that class.
class MyClass:
    attr1 = 10
    attr2 = "Hello"

print(MyClass.__dict__)

#3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class MyClass:
    def __init__(self, value):
        self.value = value

instance = MyClass(5)

print(instance.__dict__)

#4.Write a Python program that imports the abs() function using the builtins module, displays the documentation of the abs() function and finds the absolute value of -155.
import builtins

abs_function = builtins.abs

print("Dokumentacja funkcji abs:")")
print(abs_function.__doc__)

print("Wartość bezwzględna z -155:")
print(abs_function(-155))

#5.Define a Python function student(). Using function attributes display the names of all arguments.
def student(name, age, class_name):
    pass

print(student.__code__.co_varnames)

#6. Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    if student_name:
        print(f"Student Name: {student_name}")
    if student_class:
        print(f"Student Class: {student_class}")

print("Wyświetlanie danych studenta:")
student_data(12345)
student_data(12345, student_name="JANEK")
student_data(12345, student_name="ADAM", student_class="")

#7. Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

print("Typ klasy Student::")
print(type(Student))

print("Klucze atrybutu __dict__")
print(Student.__dict__.keys())

print("Wartość atrybutu __module__")
print(Student.__module__)

#8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances
# of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

print("Czy instancja_studenta jest instancją klasy Student?")
print(isinstance(student_instance, Student))

print("Czy instancja_ocen jest instancją klasy Marks")
print(isinstance(marks_instance, Marks))

print("Czy Student jest podklasą object?")
print(issubclass(Student, object))

print("Czy Marks jest podklasą object?")
print(issubclass(Marks, object))

#9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Jacek", 85)

print("Oryginalne wartości:")
print("Student Name :", student.student_name)
print("Marks:", student.marks)

student.student_name = "Arek"
student.marks = 90

print("Zmodyfikowane wartości ")
print("Student Name :", student.student_name)
print("Marks:", student.marks)

#10. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute
# and the values of the class. Now remove the student_name attribute and display the entire attribute with values.
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(1, "Arek")
student.student_class = "5"

print("Wszystkie atrybuty i ich wartości:")
print(student.__dict__)

del student.student_name

print("Po usunięciu atrybutu student_name:")
print(student.__dict__)

#11. Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Wszystkie atrybuty:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Student(1, "arek")
student.student_class = "5"

student.display_attributes()

#12. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "arek")
student2 = Student(2, "Janek")

print(f"Student 1 - ID: {student1.student_id}, Name: {student1.student_name}")
print(f"Student 2 - ID: {student2.student_id}, Name: {student2.student_name}")

#Python class, Basic application

#1. Write a Python class to convert an integer to a Roman numeral.
class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        roman = ''
        for value, symbol in self.value_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman
converter = IntegerToRoman()
print(converter.int_to_roman(1994))

#2. Write a Python class to convert a Roman numeral to an integer.
class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in s[::-1]:
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

converter = RomanToInteger()
print(converter.roman_to_int("MCMXCIV"))

#3. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if stack == [] or bracket_map[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

validator = ParenthesesValidator()
print(validator.is_valid("()[]{}"))
print(validator.is_valid("([)]"))

#4. Write a Python class to get all possible unique subsets from a set of distinct integers.
class Subsets:
    def unique_subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result


subsets_generator = Subsets()
print(subsets_generator.unique_subsets([4, 5, 6]))

#5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
class PairSum:
    def two_sum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i


finder = PairSum()
print(finder.two_sum([10, 20, 10, 40, 50, 60, 70], 50))

#6. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
class ThreeSum:
    def three_sum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

finder = ThreeSum()
print(finder.three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))

#7. Write a Python class to implement pow(x, n).
class Power:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

power_calculator = Power()
print(power_calculator.my_pow(2, 10))

#8. Write a Python class to reverse a string word by word.
class StringReverser:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])


reverser = StringReverser()
print(reverser.reverse_words('hello .py'))

#9. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
class StringManipulator:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Enter a string: ")

    def print_String(self):
        print(self.s.upper())

manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()

#10. Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 5)
print(rect.area())

#11. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(3)
print(circle.area())
print(circle.perimeter())

#12. Write a Python program to get the class name of an instance in Python.
class ExampleClass:
    pass

instance = ExampleClass()
print(instance.__class__.__name__)

#Python class, Real-life problems

#1.Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
 class Pracownik:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def przypisz_dzial(self, nowy_dzial):
        self.emp_department = nowy_dzial

    def drukuj_dane_pracownika(self):
        print("Dane pracownika:")
        print(f"ID: {self.emp_id}")
        print(f"Imię i nazwisko: {self.emp_name}")
        print(f"Pensja: {self.emp_salary} PLN")
        print(f"Dział: {self.emp_department}")

    def oblicz_pensje(self, pensja, godziny_przepracowane):
        if godziny_przepracowane > 50:
            nadgodziny = godziny_przepracowane - 50
            nadgodziny_kwota = (nadgodziny * (pensja / 50))
            pensja += nadgodziny_kwota
        return pensja

dane_pracownikow = [
    ("ADAMS", "E7876", 50000, "KSIĘGOWOŚĆ"),

]

pracownicy = []
for emp_name, emp_id, emp_salary, emp_department in dane_pracownikow:
    pracownik = Pracownik(emp_name, emp_id, emp_salary, emp_department)
    pracownicy.append(pracownik)

print("Przed zmianą działu:")
for pracownik in pracownicy:
    pracownik.drukuj_dane_pracownika()

print("Po zmianie działu:")
pracownicy[0].przypisz_dzial("FINANSE")
for pracownik in pracownicy:
    pracownik.drukuj_dane_pracownika()

print("Obliczanie pensji:")
pensja = pracownicy[0].oblicz_pensje(50000, 55)
print(f"Pensja po uwzględnieniu nadgodzin: {pensja} PLN")

#2. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
class Restauracja:
    def __init__(self):
        self.menu = {}
        self.zarezerwowane_stoly = []
        self.zamowienia_klientow = []

    def dodaj_do_menu(self, danie, cena):
        self.menu[danie] = cena

    def zarezerwuj_stol(self, numer_stolu):
        self.zarezerwowane_stoly.append(numer_stolu)

    def zamowienie_klienta(self, numer_stolu, dania):
        self.zamowienia_klientow.append({'numer_stolu': numer_stolu, 'dania': dania})

    def drukuj_menu(self):
        print("Menu:")
        for danie, cena in self.menu.items():
            print(f"{danie}: {cena} zł")

    def drukuj_zarezerwowane_stoly(self):
        print("Zarezerwowane stoły:")
        print(self.zarezerwowane_stoly)

    def drukuj_zamowienia_klientow(self):
        print("Zamówienia klientów:")
        for zamowienie in self.zamowienia_klientow:
            print(f"Stolik {zamowienie['numer_stolu']} zamówił: {zamowienie['dania']}")



restauracja = Restauracja()


restauracja.dodaj_do_menu("Pizza", 12.99)
restauracja.dodaj_do_menu("Burger", 8.99)
restauracja.dodaj_do_menu("Sałatka", 6.99)


restauracja.zarezerwuj_stol(1)
restauracja.zarezerwuj_stol(2)


restauracja.zamowienie_klienta(1, ["Pizza", "Sałatka"])
restauracja.zamowienie_klienta(2, ["Burger"])


restauracja.drukuj_menu()


restauracja.drukuj_zarezerwowane_stoly()

restauracja.drukuj_zamowienia_klientow()

#3. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class KontoBankowe:
    def __init__(self, numer_konta, saldo, data_otwarcia, nazwa_klienta):
        self.numer_konta = numer_konta
        self.saldo = saldo
        self.data_otwarcia = data_otwarcia
        self.nazwa_klienta = nazwa_klienta

    def wplac(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            print(f"Pomyślnie wpłacono ${kwota}. Nowe saldo: ${self.saldo}")
        else:
            print("Nieprawidłowa kwota wpłaty. Podaj dodatnią wartość.")

    def wyplac(self, kwota):
        if 0 < kwota <= self.saldo:
            self.saldo -= kwota
            print(f"Pomyślnie wypłacono ${kwota}. Nowe saldo: ${self.saldo}")
        else:
            print("Niewystarczające środki lub nieprawidłowa kwota wypłaty.")

    def sprawdz_saldo(self):
        print(f"Bieżące saldo konta {self.numer_konta}: ${self.saldo}")


konto = KontoBankowe("123456789", 1000, "2024-05-31", "Jan Kowalski")

konto.wplac(500)
konto.wyplac(200)
konto.sprawdz_saldo()

#4. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
class Inwentarz:
    def __init__(self):
        self.przedmioty = {}

    def dodaj_przedmiot(self, id_przedmiotu, nazwa_przedmiotu, ilosc_w_magazynie, cena):
        self.przedmioty[id_przedmiotu] = {'nazwa': nazwa_przedmiotu, 'ilosc': ilosc_w_magazynie, 'cena': cena}

    def aktualizuj_przedmiot(self, id_przedmiotu, nazwa_przedmiotu=None, ilosc_w_magazynie=None, cena=None):
        if id_przedmiotu in self.przedmioty:
            if nazwa_przedmiotu is not None:
                self.przedmioty[id_przedmiotu]['nazwa'] = nazwa_przedmiotu
            if ilosc_w_magazynie is not None:
                self.przedmioty[id_przedmiotu]['ilosc'] = ilosc_w_magazynie
            if cena is not None:
                self.przedmioty[id_przedmiotu]['cena'] = cena
        else:
            print(f"Przedmiot o ID {id_przedmiotu} nie znaleziono w inwentarzu.")

    def szczegoly_przedmiotu(self, id_przedmiotu):
        if id_przedmiotu in self.przedmioty:
            print(f"ID Przedmiotu: {id_przedmiotu}")
            print(f"Nazwa Przedmiotu: {self.przedmioty[id_przedmiotu]['nazwa']}")
            print(f"Ilość w Magazynie: {self.przedmioty[id_przedmiotu]['ilosc']}")
            print(f"Cena: {self.przedmioty[id_przedmiotu]['cena']} PLN")
        else:
            print(f"Przedmiot o ID {id_przedmiotu} nie znaleziono w inwentarzu.")



inwentarz = Inwentarz()

inwentarz.dodaj_przedmiot("ITM001", "Laptop", 10, 999.99)
inwentarz.dodaj_przedmiot("ITM002", "Smartfon", 20, 599.99)

inwentarz.aktualizuj_przedmiot("ITM001", ilosc_w_magazynie=8)
inwentarz.aktualizuj_przedmiot("ITM003", nazwa_przedmiotu="Tablet")

inwentarz.szczegoly_przedmiotu("ITM001")
inwentarz.szczegoly_przedmiotu("ITM002")
inwentarz.szczegoly_przedmiotu("ITM003")