person = {
  "name": "Arthur",
  "age": 25,
  "city": "São Paulo",
}

print('Person: ', person)
print('Person name: ', person['name'])
print('Person age: ', person['age'])
print('Person city: ', person['city'])

person['surname'] = 'Pereira Machado'
print('Person surname: ', person['surname'])

person['age'] = 26
print('Person age: ', person['age'])

# Removing a property
del person['city']
print('Person: ', person)

# Keys() -> return all the keys of a dictionary
keys = list(person.keys())
print('Keys: ', keys)
print('First key: ', keys[0])

# Values() -> return all the values of a dictionary
values = list(person.values())
print('Values: ', values)
print('First value: ', values[0])

# Items() -> return each key-value pair as a tuple
items = list(person.items())
print('Items: ', items)
print('Items first index: ', items[0])
print('Key of first index: ', items[0][0])
print('Value of first index: ', items[0][1])
print('Key-value: %s = %s ' % (items[1][0], items[1][1]))

# OBS: The list before each method is because the method only refers to the dictionary
# so it is not saved on memory, therefore you cant access it directly