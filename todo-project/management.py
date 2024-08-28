def add_task(tasks: list, task_name):
  task = {
    "task": task_name,
    "completed": False
  }

  tasks.append(task)
  print(f'Tasks {task_name} was added successfully')
  return

tasks = []
while True:
  print('\n Todo List Management Menu:')
  print('1. Adding new task')
  print('2. List tasks')
  print('3. Update task')
  print('4. Finish task')
  print('5. Delete completed tasks')
  print('6. Exit program')

  option = int(input('Choose an option: '))

  if option == 1:
    task_name = input('Enter task name:')
    add_task(tasks, task_name)
  elif option == 6:
    break

print('Finished program')