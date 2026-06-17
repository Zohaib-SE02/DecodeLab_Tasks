todo_list = []
task_id = 1

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Add Remark")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")

        todo_list.append({
            "id": task_id,
            "task": task,
            "remark": "Not Done"
        })

        print("Task added with ID:", task_id)
        task_id += 1

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            for item in todo_list:
                print(f"ID: {item['id']} | Task: {item['task']} | Remark: {item['remark']}")

    elif choice == "3":
        id_no = int(input("Enter Task ID: "))

        for item in todo_list:
            if item["id"] == id_no:
                item["remark"] = input("Enter remark (Done/Not Done): ")
                print("Remark updated!")
                break
        else:
            print("Task ID not found.")

    elif choice == "4":
        id_no = int(input("Enter Task ID to delete: "))

        for item in todo_list:
            if item["id"] == id_no:
                todo_list.remove(item)
                print("Task deleted!")
                break
        else:
            print("Task ID not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")