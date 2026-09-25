numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Add an element at the end
numbers.append(60)
print("After append:", numbers)

# Add multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# Insert an element at a specific position
numbers.insert(1, 15)
print("After insert:", numbers)

# Access an element
print("First element:", numbers[0])

# Update an element
numbers[0] = 5
print("After update:", numbers)

# Search for an element
if 30 in numbers:
    print("30 is present in the list.")

# Find index
print("Index of 40:", numbers.index(40))

# Count an element
numbers.append(40)
print("Count of 40:", numbers.count(40))

# Remove an element by value
numbers.remove(40)
print("After remove:", numbers)

# Remove the last element
removed_element = numbers.pop()
print("Removed element:", removed_element)
print("After pop:", numbers)

# Sort in ascending order
numbers.sort()
print("Ascending order:", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)

# Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# Copy the list
new_numbers = numbers.copy()
print("Copied list:", new_numbers)

# List slicing
print("First three elements:", numbers[:3])

# List length
print("Length of list:", len(numbers))

# Clear the list
numbers.clear()
print("After clear:", numbers)


# Copy the list
import copy as c

original = [
    ["Arun", 85],
    ["Priya", 92]
]

shallow = original.copy() # A shallow copy creates a new outer collection, but the nested objects inside are still shared
deep = c.deepcopy(original) #A deep copy creates a new outer collection and new copies of all nested objects.

shallow[0][1] = 100
print("Original after shallow copy change:", original)

deep[1][1] = 95
print("Original after deep copy change:", original)
print("after deep copy change:", deep)