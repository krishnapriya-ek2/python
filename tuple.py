# Program to create a list and tuple from comma-separated numbers
numbers = input("Enter comma-separated numbers: ")
# Convert input into a list
my_list = numbers.split(",")
# Convert list into a tuple
my_tuple = tuple(my_list)
# Display list and tuple
print("List:", my_list)
print("Tuple:", my_tuple)
# Total number of elements
print("Total number of elements:", len(my_list))
# First and last elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])
# List in reverse order
print("List in reverse order:", my_list[::-1])