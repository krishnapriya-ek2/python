# Program to perform operations on dictionaries and sets

# 1. Creating dictionaries
dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"mango": 4, "grape": 6}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# 2. Sorting dictionary by values
sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1]))
print("Sorted dictionary:", sorted_dict)

# 3. Merging dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged dictionary:", merged_dict)

# 4. Frequency counting using dictionary
text = input("Enter a word: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:", frequency)

# 5. Creating sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Set 1:", set1)
print("Set 2:", set2)

# 6. Common elements
common = set1.intersection(set2)
print("Common elements:", common)

# 7. Unique elements
unique = set1.symmetric_difference(set2)
print("Unique elements:", unique)