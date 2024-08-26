# Declaration

list = [1, 2, 3, 4, 5, "test", True, False]

print("List: ", list)
print("List at index 0: ", list[0])
print("List at index 5: ", list[5])
print("Sliced list[1:6]: ", list[1:6]) # Output: [2, 3, 4, 5, "test"]
print("Sliced list[:5]: ", list[:5]) # Output: [1, 2, 3, 4, 5]
print("Sliced list[5:]: ", list[5:]) # Output: ["test", True, False]

list[0] = "python"
print("List changed: ", list)

# Methods

# Append: add element at the end of the list
list.append("new")
print("List with append: ", list)

# Index
index = list.index("test")
print("Index 6: ", index)

# Insert: insert an element at a specific index
list.insert(2, "insert")
print("List with insert: ", list)

# Pop: remove an element at a specific index and return this element
popped_element = list.pop(4)
print("Popped element: ", popped_element)
print("List with pop: ", list)

# Remove: remove the first element or the specified element
list.remove(False)
print("List with remove: ", list)

# Sort ascending
list_numbers = [1, 5, 3, 2, 4]
list_numbers.sort()
print("List with sort ascending: ", list_numbers)

# Sort descending
list_numbers.sort(reverse=True)
print("List with sort descending: ", list_numbers)