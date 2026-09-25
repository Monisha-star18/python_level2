student = {
    "name": "Monisha",
    "age": 20,
    "course": "Python",
    "mark": 90
}

print("Original dictionary:", student)

# Access values
print("Student name:", student["name"])
print("Student mark:", student["mark"])

# Access using get()
print("Student age:", student.get("age")) #no key error if not avalibe  give none

# Add a new key-value pair
student["city"] = "Coimbatore"
print("After adding city:", student)

# Update a value
student["mark"] = 95
print("After updating mark:", student)

# Add multiple values
student.update({
    "college": "ABC College",
    "year": 2
})
print("After update:", student)

# Check whether a key exists
if "name" in student:
    print("Name key is present.")

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())

# Display key-value pairs
print("Items:", student.items())

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Remove a key-value pair
removed_value = student.pop("year")
print("Removed value:", removed_value)
print("After pop:", student)

# Remove the last inserted item
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem:", student)

# Copy dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# Length of dictionary
print("Number of items:", len(student))

# Clear dictionary
student.clear()
print("After clear:", student)