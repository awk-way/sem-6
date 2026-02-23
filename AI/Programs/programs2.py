# 1. Take a string input and print it.
s = input("Enter a string: ")
print("Entered string:", s)

# 2. Find the length of a string.
s = input("Enter a string: ")
print("Length of string:", len(s))

# 3. Print each character of a string on a new line.
s = input("Enter a string: ")
print("Characters on new lines:")
for ch in s:
    print(ch)

# 4. Count the number of characters in a string (without using len()).
s = input("Enter a string: ")
count = 0
for ch in s:
    count += 1
print("Character count (without len):", count)

# 5. Convert a string to uppercase.
s = input("Enter a string: ")
print("Uppercase:", s.upper())

# 6. Convert a string to lowercase.
s = input("Enter a string: ")
print("Lowercase:", s.lower())

# 7. Check whether a string is empty or not.
s = input("Enter a string: ")
if s == "":
    print("String is empty")
else:
    print("String is not empty")

# 8. Count the number of vowels in a string.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 9. Count the number of consonants in a string.
consonant_count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        consonant_count += 1
print("Number of consonants:", consonant_count)

# 10. Check whether a string contains only digits.
s = input("Enter a string: ")
if s.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")

# 11. Check whether a string starts with a vowel.
s = input("Enter a string: ")
if s != "" and s[0] in vowels:
    print("String starts with a vowel")
else:
    print("String does not start with a vowel")

# 12. Check whether a string ends with a consonant.
if s != "" and s[-1].isalpha() and s[-1] not in vowels:
    print("String ends with a consonant")
else:
    print("String does not end with a consonant")

# 13. Count how many times a given character appears in a string.
s = input("Enter a string: ")
char = input("Enter character to count: ")
print("Occurrences:", s.count(char))

# 14. Reverse a string using a loop.
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

# 15. Check whether a string is a palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# 16. Count the number of words in a string.
s = input("Enter a string: ")
words = s.split()
print("Number of words:", len(words))

# 17. Find the first repeated character in a string.
s = input("Enter a string: ")
seen = set()
first_repeat = None
for ch in s:
    if ch in seen:
        first_repeat = ch
        break
    seen.add(ch)
if first_repeat:
    print("First repeated character:", first_repeat)
else:
    print("No repeated character found")

# 18. Remove all spaces from a string.
s = input("Enter a string(with spaces): ")
no_spaces = s.replace(" ", "")
print("String without spaces:", no_spaces)

# 19. Replace all vowels with *
s = input("Enter a string: ")
new_string = ""
for ch in s:
    if ch in vowels:
        new_string += "*"
    else:
        new_string += ch
print("Vowels replaced with *:", new_string)

# 20. Sort characters of a string alphabetically.
s = input("Enter a string: ")
sorted_string = "".join(sorted(s))
print("Alphabetically sorted string:", sorted_string)