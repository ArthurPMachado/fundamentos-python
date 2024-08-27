numbersList = [1, 2, 3, 4, 5]
for number in numbersList:
  print("List: ", number)

numbersTuple = (1, 2, 3, 4, 5)
for number in numbersTuple:
  print("Tuple: ", number)

person = {
  "name": "Arthur",
  "age": 25,
  "city": "São Paulo",
}

print('\nFor using dictionary keys')
for key in person.keys():
  print("Key: ", key)

print('\nFor using dictionary values')
for value in person.values():
  print('Value: ', value)

print('\nFor using dictionary items')
for key, value in person.items():
  print(f"{key} = {value}")

# range() -> return an numbered interval
# [0,1,2,3,4,5,6,7,8,9]
print('\nFor using range()')
for number in range(5):
  print('Number: ', number)

print('\nFor using range() with len()')
for index in range(0, len(numbersList)):
  print('Index: ', index)
  print('Element: ', numbersList[index])
  if index == 3:
    numbersList[index] = 100
  else:
    numbersList[index] = 0

print(numbersList)

# enumerate() -> return the index and the value of a list
print('\nFor using enumerate')
enumerate_list = ['a', 'b', 'c']
for index, value in enumerate(enumerate_list):
  print(f'{index} = {value}')
  if index == 1:
    print('Index 1')