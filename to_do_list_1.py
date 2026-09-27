tasks = []


def show_menu():
    print("\n" + "=" * 30)
    print("        TO-DO LIST")
    print("=" * 30)
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Exit")
    print("=" * 30)


def add_task():
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print(f"✓ Added: {title}")


def show_tasks():
    if not tasks:
        print("\nYour list is empty. Nothing to do... yet.")
        return

    print("\n--- Your Tasks ---")

    for number, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{number}. [{status}] {task['title']}")


def complete_task():
    if not tasks:
        print("There are no tasks to complete.")
        return

    show_tasks()

    try:
        number = int(input("\nWhich task did you complete? "))

        if number < 1 or number > len(tasks):
            print("That task does not exist.")
            return

        task = tasks[number - 1]

        if task["completed"]:
            print("That task is already completed.")
            return

        task["completed"] = True
        print(f"✓ Completed: {task['title']}")

    except ValueError:
        print("Please enter a number.")


def main():
    print("\nWelcome to your To-Do List.")

    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            print("\nGoodbye. Go do the tasks.\n")
            break

        else:
            print("Invalid choice. Please choose 1–4.")


main()