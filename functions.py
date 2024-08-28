def welcome(name):
  print(f"Welcome {name}")

print('\nCalling function: ')
welcome('Arthur')
welcome('Test')

# Function with return
def squared(number):
  result = number ** 2
  return result

print('\nCalling function squared: ')
squared_result = squared(10)
print(squared_result)

# Function with multiple params
def sum(number1, number2):
  result = number1 + number2
  return result

print('\nCalling function sum: ')
number1 = 10
number2 = 20
sum_result = sum(number1, number2)
print('The sum of number %s and the number %s is %s' % (number1, number2, sum_result))