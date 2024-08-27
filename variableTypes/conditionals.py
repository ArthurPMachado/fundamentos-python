# if, elif and else

# If
age = 18
if age >= 18:
  print("Legal age")

if age == 18:
  print('You are 18 years old')

if age < 18:
  print('Minor')

if age != 10:
  print('You are not 10 years old')

# Else and elif
another_age = 11
if another_age >= 18:
  print("Legal age")
elif another_age >= 12:
  print('You are a teenager')
else:
  print('You are a child')

message = "Can have a beer" if another_age >= 18 else "Cannot have a beer"
print(message)