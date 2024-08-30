print('Example of exception')
try:
  number = int(input('Enter a integer number: '))
  result = 10 / number
except ValueError as error:
  print(f'Exception of value error {error}')
  raise ValueError('Variable type is not a number')
except Exception as error:
  print(f'Error: {error}')
else:
  print(f'Result {result}')
finally:
  print('End of program')