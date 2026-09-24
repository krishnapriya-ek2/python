# Program to perform list operations

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Searching an element
search = int(input("Enter a number to search: "))

if search in numbers:
    print(search, "is present in the list")
else:
    print(search, "is not present in the list")

# Updating an element
numbers[1] = 25
print("After updating:", numbers)

# Adding an element
numbers.append(60)
print("After adding:", numbers)

# Removing an element
numbers.remove(30)
print("After removing:", numbers)

# List comprehension - filtering even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Sorting the list
numbers.sort()
print("Sorted list:", numbers)

# Reversing the list
numbers.reverse()
print("Reversed list:", numbers)