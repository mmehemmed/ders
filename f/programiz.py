# Python Program to Print Hello World!
print("Helo World!")

# Python Program to Add Two Numbers
a = 5
b = 3
print(a + b)

# Python Program to Find the Square Root
x = 16
print(x ** 0.5)

# Python Program to Calculate the Area of a Triangle
base = 5
height = 10
print(0.5 * base * hieght)

# Python Program to Solve Quadratic Equation
import cmath
a = 1
b = 5
c = 6
d = (b ** 2) - (4 * a * c)
sol1 = (-b + cmath.sqrt(d)) / (2 * a)
sol2 = (-b - cmath.sqrt(d)) / (2 * a)
print(sol1, sol2)

# Python Program to Swap Two Variables
a = 5
b = 10
a, b = b, a
print(a, b)

# Python Program to Generate a Random Number
import random
print(random.randint(1, 100))

# Python Program to Convert Kilometers to Miles
km = 5
miles = km * 0.621371
print(miles)

# Python Program to Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenhiet)

# Python Program to Check if a Number is Positive, Negative or 0
num = -7
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Python Program to Check if a Number is Odd or Even
num = 7
print("Even" if num % 2 == 0 else "Odd")

# Python Program to Check Leap Year
year = 2000
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Python Program to Find the Largest Among Three Numbers
a, b, c = 10, 20, 15
print(max(a, b, c))

# Python Program to Check Prime Number
num = 29
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Python Program to Print all Prime Numbers in an Interval
start, end = 10, 20
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Python Program to Find the Factorial of a Number
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

# Python Program to Display the Multiplication Table
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Python Program to Print the Fibonacci Sequence
n = 10
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

# Python Program to Check Armstrong Number
num = 153
order = len(str(num))
sum = sum(int(digit) ** order for digit in str(num))
print("Armstrong" if sum == num else "Not Armstrng")

# Python Program to Find Armstrong Number in an Interval
start, end = 100, 200
for num in range(start, end + 1):
    order = len(str(num))
    sum = sum(int(digit) ** order for digit in str(num))
    if sum == num:
        print(num)

# Python Program to Find the Sum of Natural Numbers
n = 10
print(n * (n + 1) // 2)

# Python Program to Display Powers of 2 Using Anonymous Function
n = 5
powers = [2 ** i for i in range(n)]
print(powers)

# Python Program to Find Numbers Divisible by Another Number
nums = [10, 20, 33, 46, 55]
check = 5
result = [num for num in nums if num % check == 0]
print(result)

# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
num = 10
print(bin(num), oct(num), hex(num))

# Python Program to Find ASCII Value of Character
char = 'A'
print(ord(char))

# Python Program to Find HCF or GCD
a, b = 60, 48
while b:
    a, b = b, a % b
print(a)

# Python Program to Find LCM
a, b = 12, 15
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
print(a * b // gcd(a, b))

# Python Program to Find the Factors of a Number
num = 28
factors = [i for i in range(1, num + 1) if num % i == 0]
print(factors)

# Python Program to Make a Simple Calculator
def calculator(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
print(calculator(10, 5, '+'))

# Python Program to Shuffle Deck of Cards
import itertools, random
deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Diamonds', 'Clubs']))
random.shuffle(deck)
print(deck[:5])

# Python Program to Display Calendar
import calendar
print(calendar.month(2023, 12))

# Python Program to Display Fibonacci Sequence Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
for i in range(n):
    print(fibonacci(i))

# Python Program to Find Sum of Natural Numbers Using Recursion
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)
print(sum_natural(10))

# Python Program to Find Factorial of Number Using Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Python Program to Convert Decimal to Binary Using Recursion
def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')
decimal_to_binary(10)
print()

# Python Program to Add Two Matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(result)

# Python Program to Transpose a Matrix
matrix = [[1, 2], [3, 4]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

# Python Program to Multiply Two Matrices
X = [[1, 2], [3, 4]]
Y = [[5, 6], [7, 8]]
result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
print(result)

# Python Program to Check Whether a String is Palindrome or Not
string = "radar"
print("Palindrome" if string == string[::-1] else "Not Palindrome")

# Python Program to Remove Punctuations from a String
string = "Hello, World!"
punctuations = "!()-[]{};:'\,<>./?@#$%^&*_~"
result = "".join(char for char in string)
