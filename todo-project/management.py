def add_task(tasks: list, task_name):
  task = {
    "task": task_name,
    "completed": False
  }

  tasks.append(task)
  print(f'Tasks {task_name} was added successfully')
  return

def list_tasks(tasks: list):
  print("\nTasks List: ")
  for index, task in enumerate(tasks, start=1):
    status = '✔' if task['completed'] else '✘'
    task_name = task['task']
    print(f'{index}. [{status}] {task_name}')

  return

def update_task_name(tasks: list, task_index, new_task_name):
  adjust_index = int(task_index) - 1

  if adjust_index >= 0 and adjust_index < len(tasks):
    tasks[adjust_index]['task'] = new_task_name

    print(f'Task {task_index} was updated to {new_task_name}')
    return
  
  print('Invalid task index')
  return

def complete_task(tasks: list, task_index):
  adjust_index = int(task_index) - 1

  if adjust_index >= 0 and adjust_index < len(tasks):
    tasks[adjust_index]['completed'] = True

    print(f'Task {task_index} marked as completed')
    return
  
  print('Invalid task index')
  return

def delete_completed_tasks(tasks: list):
  tasks_not_completed = []

  for task in tasks:
    if not task['completed']:
      tasks_not_completed.append(task)

  print('Completed tasks deleted')

  return tasks_not_completed

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
    task_name = input('Enter task name: ')
    add_task(tasks, task_name)

  elif option == 2:
    list_tasks(tasks)

  elif option == 3:
    list_tasks(tasks)
    task_index = input('Enter tasks index to be updated: ')
    new_name = input('Enter new task name: ')
    update_task_name(tasks, task_index, new_name)
  
  elif option == 4:
    list_tasks(tasks)
    task_index = input('Enter tasks index to be completed: ')
    complete_task(tasks, task_index)

  elif option == 5:
    tasks_not_completed = delete_completed_tasks(tasks)
    tasks = tasks_not_completed
    list_tasks(tasks)

  elif option == 6:
    break

print('Finished program')