my_tuple = (1, 2, 2, 3, 4)

print("Tuple: ", my_tuple)
print("Tuple at index 0: ", my_tuple[0])
print("Sliced tuple: ", my_tuple[1:3])
print("Negative tuple: ", my_tuple[-1])

# Count: return the number of occurrences of an element
count = my_tuple.count(2)
print("Count tuple: ", count)

index = my_tuple.index(2)
print("Index tuple: ", index)