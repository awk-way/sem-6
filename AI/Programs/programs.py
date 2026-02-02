# 1. Print “Hello, World!” on the screen.
print("Hello World!")

# 2. Declare variables of different types (int, float, string) and print their values and types.
a = 25
b = 74.245
c = "Computer"
d = True
e = ["Java", "Python", "C++"]
f = ("HTML", "CSS", "JavaScript")
g = {"semester" : "6", "subject" : "AI"}
print("\n", a, type(a), "\n", b, type(b), "\n", c, type(c), "\n", d, type(d), "\n", e, type(e), "\n", f, type(f), "\n", g, type(g), "\n")

# 3. Take two numbers as input and perform addition, subtraction, multiplication, division, and modulus.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition of",num1,"and",num2,"=",num1 + num2)
print("Subtraction of",num2,"from",num1,"=",num1 - num2)
print("Multiplication of",num1,"and",num2,"=",num1 * num2)
print("Division of",num1,"by",num2,"=",num1 / num2)
print("Modulus of",num1,"and",num2,"=",num1 % num2)

# 4. Swap two numbers using a temporary variable and without a temporary variable.
temp = num1
num1 = num2
num2 = temp
print("\nAfter swapping the two input numbers using a temporary variable: num1 = ",num1,"\tnum2 = ",num2)
num1, num2 = num2, num1
print("After swapping the two input numbers without a temporary variable: num1 = ",num1,"\tnum2 = ",num2)

# 5. Input a number and check if it is even or odd.
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Entered number",num,"is Even")
else:
    print("Entered number",num,"is Odd")

# 6. Find the largest number among three input numbers using if-else statements.
x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x >= y and x >= z:
    print("Number",x,"is the largest number")
elif y >= x and y >= z:
    print("Number",y,"is the largest number")
else:
    print("Number",z,"is the largest number")

# 7. Implement a calculator that can perform +, -, *, / operations based on user input.
x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
o = input("Enter operator(+, -, *, /): ")
if o == "+":
    print(x, o, y, "=", x + y)
elif o == "-":
    print(x, o, y, "=", x - y)
elif o == "*":
    print(x, o, y, "=", x * y)
elif o == "/":
    print(x, o, y, "=", x / y)
else:
    print("Invalid operator")

# 8. Determine whether a given year is a leap year or not.
yr = int(input("\nEnter a year: "))
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")

# 9. Display multiplication tables from 1 to 10 using loops.
print("\nMultiplication tables from 1 to 10:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{j} x {i} = {j*i:<3}", end="\t")
    print()

# 10. Compute the factorial of a number using a loop.
num = int(input("\nEnter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of",num,"=",fact)

# 11. Generate the first n terms of the Fibonacci sequence.
n = int(input("\nEnter number of terms of the Fibonacci sequence: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 12. Calculate the sum of the digits of a given number.
num = int(input("\nEnter a number: "))
n, sumd = num, 0
while n > 0:
    sumd += n % 10
    n //= 10
print("Sum of digits of",num,"=",sumd)

# 13. Reverse a given number and print it.
n, rev = num, 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("\nReverse of ",num,"=",rev)

# 14. Check if a number or string is a palindrome.
s = input("\nEnter a string or number: ")
if s == s[::-1]:
    print("Entered input is a palindrome")
else:
    print("Entered input is not palindrome")

# 15. Check whether a given number is prime.
num = int(input("\nEnter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num,"is not q prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# 16. Create a list, append elements, remove elements, find sum, max, min, and sort the list.
lst = [50, 26, 84]
lst.append(42)
lst.remove(50)
print("\nList:", lst)
print("Sum of elements in List:", sum(lst))
print("Largest element in the list:", max(lst))
print("Smallest element in the list:", min(lst))
lst.sort()
print("Sorted list:", lst)

# 17. Create a tuple, access elements, and demonstrate immutability.
t = ("HTML", "CSS", "JavaScript")
print("\nTuple:", t)
print("Element at index 1:", t[1])
# t[1] = 5  # this will give an error as tuple is immutable

# 18. Create a dictionary, add and remove key-value pairs, and iterate through it.
d = {"semester" : "6", "subject" : "AI"}
d["credits"] = 3
del d["semester"]
print("\nDictionary:")
for key, value in d.items():
    print(key, value)

# 19. Take a string input and perform operations like length, slicing, reversing, and counting vowels.
s = input("\nEnter a string: ")
print("Length of string:", len(s))
print("Slicing string:", s[1:4])
print("Reversed string:", s[::-1])

vowels = "aeiouAEIOU"
c= 0
for ch in s:
    if ch in vowels:
        c += 1
print("Number of vowels in",s,":",c)

# 20. Write a Python program with a function to calculate the area of a circle, rectangle, and triangle.
def a_circle(r):
    return 3.14 * r * r

def a_rectangle(l, w):
    return l * w

def a_triangle(b, h):
    return 0.5 * b * h

print("\nArea of Circle:", a_circle(5))
print("Area of Rectangle:", a_rectangle(4, 6))
print("Area of Triangle:", a_triangle(3, 7))