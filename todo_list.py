'''
TO-DO List Application:
    Write a program to create a simple To-Do List application. The program allows users to 
    add tasks, view the current list of tasks, and remove tasks once they are completed.
    
    Optional Enhancements
        • Add an option in the menu that allows users to mark tasks as completed instead of removing 
        them. Completed tasks can be displayed separately or removed from the list.
        
        • Implement functionality that saves the list to a file and loads it when the
        program starts. This way, users can maintain their to-do list across different sessions.
        
        • Allow users to categorize tasks (e.g., Work, Personal) and filter the list based
        on these categories. This adds an organizational element to the to-do list.
'''
# Print To-do list menu:

task_actions = ['1. View Tasks', '2. Add a Task', '3. Remove a Task', '4. Exit']

def get_response():
    print('Todo List Menu: ')
    for action in task_actions:
        print(action)

    while True:
        selection = int(input('Enter your choice: '))
        if selection not in [1, 2, 3, 4]:
            print('Invalid Choice.')
            continue
        else:
            return selection

def view_tasks(tasks):
    task_number = 1
    print('Here are the tasks in your To-Do: ')
    for task in tasks:
        print(f'    {task_number}. {task}')
        task_number += 1
    return

def add_task(tasks):
    new_task = input('Enter a new task: ').strip()
    tasks.append(new_task)
    return tasks

def remove_task(tasks):
    print('Here are the list of tasks. Please select task to remove: ')
    view_tasks(tasks)

    while True:
        selection = int(input('Enter a task numebr to remove: '))
        if selection not in [i+1 for i in range(len(tasks))]:
            print('Invalid Choice.')
            continue
        else:
            del tasks[selection-1]
            return tasks

def main():
    tasks_list = []

    choise = get_response()

    while True:
        if choise == 1:
            view_tasks(tasks_list)
        elif choise == 2:
            tasks_list = add_task(tasks_list)
        elif choise == 3:
            tasks_list = remove_task(tasks_list)
            print('Here are the list of pending tasks after deleting the selection: ')
            view_tasks(tasks_list)
        elif choise == 4:
            break
        else:
            print('Selection Error.')
        choise = get_response()

if __name__ == '__main__':
    main()
