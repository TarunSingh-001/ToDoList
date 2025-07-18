
#Simple To-Do List App using Python
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]
except FileNotFoundError:
    tasks = []

while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "2":
        newtask = input("Enter a new task: ")
        if newtask.strip() != "":
            tasks.append(newtask.strip())
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print("Task added.")
        else:
            print("Task cannot be empty.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            try:
                taskno = int(input("Enter task number to remove: "))
                if 1 <= taskno <= len(tasks):
                    removed = tasks.pop(taskno - 1)
                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task + "\n")
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you! Exiting the To-Do app.")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
