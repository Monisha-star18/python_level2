numbers = {10, 20, 30, 40, 50}

print("Original set:", numbers)

# Add an element
numbers.add(60)
print("After add:", numbers)

# Add multiple elements
numbers.update({70, 80})
print("After update:", numbers)

# Duplicate elements are ignored
numbers.add(20)
print("After adding duplicate:", numbers)

# Search for an element
if 30 in numbers:
    print("30 is present in the set.")

# Remove an element
numbers.remove(10) #Raises KeyError
print("After remove:", numbers)

# Discard an element
numbers.discard(20) #Does nothing
print("After discard:", numbers)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print("Union:", set_a.union(set_b)) #all values duplicates not allowes 

# Intersection
print("Intersection:", set_a.intersection(set_b)) #common 

# Difference
print("Difference:", set_a.difference(set_b))  # a-b only a , remove if in b 

# Symmetric difference
print("Symmetric difference:",set_a.symmetric_difference(set_b)) #only non commom value s

# Subset
small_set = {1, 2}

if small_set.issubset(set_a): #Are all elements of small_set present in set_a?

    print("small_set is a subset of set_a.")

# Superset
if set_a.issuperset(small_set): #Does set_a contain all elements of small_set
    print("set_a is a superset of small_set.")


# Copy
copied_set = set_a.copy()
print("Copied set:", copied_set)

# Set length
print("Length of set:", len(set_a))

# Remove all elements
set_a.clear()
print("After clear:", set_a)