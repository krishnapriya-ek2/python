# Program to perform string processing operations

string = input("Enter a string: ")

# 1. Character Replacement
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

replaced = string.replace(old, new)
print("After character replacement:", replaced)

# 2. String Reversal
reverse = string[::-1]
print("Reversed string:", reverse)

# 3. Palindrome Checking
if string == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 4. Character Frequency
print("Character frequencies:")
for char in set(string):
    print(char, ":", string.count(char))

# 5. Word Frequency
words = string.split()

print("Word frequencies:")
for word in set(words):
    print(word, ":", words.count(word))