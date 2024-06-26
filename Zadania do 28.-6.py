#Python Unit Test: Exercises, Solutions, and Practice
#1.Write a Python unit test program to check if a given number is prime or not.
import unittest
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
class PrimeNumberTestCase(unittest.TestCase):
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        print("Liczby pierwsze:", prime_numbers)
       
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f"{number} nie jest rozpoznawane jako liczba pierwsza")
    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        print("Liczby, które nie są pierwsze:", non_prime_numbers)
        for number in non_prime_numbers:
            self.assertFalse(is_prime(number), f"{number} jest błędnie rozpoznawane jako liczba pierwsza")

if __name__ == '__main__':

    unittest.main()

#2. Write a Python unit test program to check if a list is sorted in ascending order.
import unittest
def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
class TestSortedAscending(unittest.TestCase):
    def test_sorted_list(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        print("Posortowana lista: ", lst)
        self.assertTrue(is_sorted_ascending(lst), "Lista nie jest posortowana rosnąco")
    def test_unsorted_list(self):
        lst = [5, 7, 2, 8, 1, 9]
        print("Nieposortowana lista: ", lst)
        self.assertFalse(is_sorted_ascending(lst), "Lista jest posortowana rosnąco")

if __name__ == '__main__':
    unittest.main()


#3.Write a Python unit test program that checks if two lists are equal.
import unittest
def lists_are_equal(nums1, nums2):
    return nums1 == nums2
class TestListsEquality(unittest.TestCase):
    def test_equal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        print("\nTest równych list:\n", nums1, "\n", nums2)
        self.assertTrue(lists_are_equal(nums1, nums2), "Listy nie są równe")
    def test_unequal_lists(self):
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        print("\nTest nierównych list:\n", nums1, "\n", nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "Listy są równe")
if __name__ == '__main__':
    unittest.main()
#4.Write a Python unit test program to check if a string is a palindrome.
import unittest

def is_palindrome(string):
    return string == string[::-1]

class TestPalindrome(unittest.TestCase):
    def test_palindrome_string(self):
        palindrome = "madam"
        print("Tekst jest  palindrom:", palindrome)
        self.assertTrue(is_palindrome(palindrome), "String nie jest palindromem")

    def test_non_palindrome_string(self):
        non_palindrome = "hello"
        print("Tekst nie jest palindrom:", non_palindrome)
        self.assertFalse(is_palindrome(non_palindrome), "String jest palindromem")

if __name__ == '__main__':
    unittest.main()
#5.Write a Python unit test program to check if a file exists in a specified directory.
import os
import unittest

def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

class TestFileExists(unittest.TestCase):
    def test_existing_file(self):
        directory = '/path/txt'
        filename = 'test1.txt'
        self.assertTrue(file_exists(directory, filename), "Plik nie istnieje w podanym katalogu")

    def test_nonexistent_file(self):
        directory = '/path/txt'
        filename = 'test2.txt'
        self.assertFalse(file_exists(directory, filename), "Plik istnieje w podanym katalogu")

if __name__ == '__main__':
    unittest.main()
#6.Write a Python unit test that checks if a function handles floating-point calculations accurately.
import unittest

class TestFloatingPointCalculations(unittest.TestCase):
    def test_addition(self):
        result = 0.3 + 0.5
        self.assertAlmostEqual(result, 0.8, places=6)

    def test_multiplication(self):
        result = 0.3 * 0.5
        self.assertAlmostEqual(result, 0.15, places=6)

    def test_division(self):
        result = 0.7 / 0.3
        self.assertAlmostEqual(result, 2.333333, places=6)

if __name__ == '__main__':
    unittest.main()

#7. Write a Python unit test program to check if a function handles multi-threading correctly.
import unittest
import threading

def perform_task():
    result = 0
    for i in range(1, 100000):
        result += i
    return result

class Test_Multi_Threading(unittest.TestCase):
    def test_multi_threading(self):
        num_threads = 10
        threads = []

        for _ in range(num_threads):
            t = threading.Thread(target=perform_task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            self.assertFalse(t.is_alive())

if __name__ == '__main__':
    unittest.main()
#8. Write a Python unit test program to check if a database connection is successful.
import unittest
import sqlite3

class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        self.assertEqual(result, (1,))

if __name__ == '__main__':
    unittest.main()

#9. Write a Python unit test program to check if a database query returns the expected results.
import unittest
import sqlite3

class TestDatabaseQuery(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
        self.conn.commit()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_database_query(self):
        self.cursor.execute("SELECT name, salary FROM employees ORDER BY name")
        results = self.cursor.fetchall()
        expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
#10.Write a Python unit test program to check if a function correctly parses and validates input data.
import unittest

def parse_and_validate_input(data):
    if isinstance(data, str) and data.isnumeric():
        return int(data) > 0
    return False

class TestInputParsing(unittest.TestCase):
    def test_valid_input(self):
        data = "100"
        result = parse_and_validate_input(data)
        self.assertTrue(result)

    def test_invalid_input(self):
        data = "Hello"
        result = parse_and_validate_input(data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

Python Exception Handling: Exercises, Solutions, and Practice
#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return result

print(divide_numbers(10, 2))  # Should print 5.0
print(divide_numbers(10, 0))  # Should print "Error: Cannot divide by zero."
print(divide_numbers(10, 5))  # Should print 2.0
#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Error: Input must be an integer.")
        else:
            return value

num = get_integer_input("Enter an integer: ")
print("You entered:", num)
#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found or cannot be opened.")
#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def multiply_numbers(x, y):
    try:
        result = x * y
    except TypeError:
        print("Error: Both inputs must be numerical.")
    else:
        return result

try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print("Result:", multiply_numbers(x, y))
except ValueError:
    print("Error: Input must be a numerical value.")
#5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open('/root/somefile.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("Error: Permission denied to open the file.")
#6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
numbers = [1, 2, 3]

try:
    print(numbers[4])
except IndexError:
    print("Error: Index is out of range.")
#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
#8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def divide_numbers(x, y):
    try:
        result = x / y
    except ArithmeticError:
        print("Error: Arithmetic error occurred.")
    else:
        return result

try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print("Result:", divide_numbers(x, y))
except ValueError:
    print("Error: Input must be a numerical value.")
#9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Unable to decode the file with specified encoding.")
except FileNotFoundError:
    print("Error: File not found or cannot be opened.")

#10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    numbers = [1, 2, 3]
    numbers.sort()
    numbers.nonexistent_method()
except AttributeError:
    print("Error: Attribute does not exist.")
Python Asynchronous Programming Exercises and Solutions
#1. Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
import asyncio

async def print_delayed_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

asyncio.run(print_delayed_message())
#2.  Write a Python program that creates three asynchronous functions and displays their respective names with different delays
import asyncio

async def print_message(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    task1 = print_message(1, "Message with 1 second delay")
    task2 = print_message(2, "Message with 2 second delay")
    task3 = print_message(3, "Message with 3 second delay")
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
#3. Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.
import asyncio

async def print_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)

asyncio.run(print_numbers())
#4. Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously using the "aiohttp" library.
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url1 = "https://www.wikipedia.org/"
    url2 = "https://www.google.com"    
    
    task1 = fetch_data(url1)
    task2 = fetch_data(url2)
    
    results = await asyncio.gather(task1, task2)
    print(results)

asyncio.run(main())
#5. Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.
import asyncio
import time

async def task1():
    await asyncio.sleep(2)
    return "Task 1 result"

async def task2():
    await asyncio.sleep(1)
    return "Task 2 result"

async def main():
    start_time = time.time()
    result1, result2 = await asyncio.gather(task1(), task2())
    end_time = time.time()
    print("Total time taken:", end_time - start_time)
    print("Result 1:", result1)
    print("Result 2:", result2)

asyncio.run(main())
#6. Write a Python program to create a coroutine that simulates a time-consuming task and use asyncio.CancelledError to handle task cancellation.
import asyncio

async def time_consuming_task():
    try:
        print("Starting time-consuming task")
        await asyncio.sleep(5)
        print("Time-consuming task completed")
    except asyncio.CancelledError:
        print("Task was cancelled")

async def main():
    task = asyncio.create_task(time_consuming_task())
    await asyncio.sleep(2)
    task.cancel()

asyncio.run(main())
#7. Write a Python program that implements a timeout for an asynchronous operation using asyncio.wait_for().
import asyncio

async def slow_operation():
    await asyncio.sleep(3)
    return "Operation completed"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print("Result:", result)
    except asyncio.TimeoutError:
        print("Timeout exceeded, operation cancelled")

asyncio.run(main())
#8. Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a single consumer.
import asyncio
async def producer(queue, id):
    for i in range(5):
        await asyncio.sleep(1)
        item = f"Item {i} from producer {id}"
        await queue.put(item)
        print(f"Produced {item}")
async def consumer(queue):
    while True:
        item = await queue.get()
        await asyncio.sleep(2)
        print(f"Consumed {item}")
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue, i)) for i in range(2)]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producers)
    await queue.join()
    consumer_task.cancel()
    await asyncio.gather(consumer_task, return_exceptions=True)
asyncio.run(main())
