# 📓 Prince Pathak's To-Do App
# Made for the grind, built for fun 💪

import os
import time

# 📁 File where tasks will be saved
FILENAME = "tasks.txt"

# 📥 Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    task, status = line.split("|")
                    tasks.append({"task": task, "done": status == "done"})
    return tasks

# 💾 Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "todo"
            file.write(f"{task['task']}|{status}\n")

# 📋 Display all tasks
def view_tasks(tasks):
    print("\n📝 Your Tasks:")
    if not tasks:
        print("📭 Nothing here yet!\n")
    else:
        for idx, t in enumerate(tasks, 1):
            status = "✅" if t["done"] else "🔲"
            print(f"{idx}. {t['task']} {status}")
    print()

# ➕ Add task(s)
def add_tasks(tasks):
    while True:
        new_task = input("➕ Enter task: ").strip()
        if new_task:
            tasks.append({"task": new_task, "done": False})
            print("✨ Task added!")
        else:
            print("⚠️ Empty task not allowed.")
        again = input("➕ Add another task? (y/n): ").lower()
        if again != "y":
            break
    print()

# ✅ Mark task complete
def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("✔️ Enter task number to mark done: "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["done"] = True
                print("🎉 Task completed!\n")
            else:
                print("⚠️ Invalid task number.\n")
        except:
            print("⚠️ Please enter a number.\n")
    time.sleep(1)

# ❌ Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("🗑️ Enter task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"🧹 Deleted: {removed['task']}\n")
            else:
                print("⚠️ Task number doesn't exist.\n")
        except:
            print("⚠️ Please enter a valid number.\n")
    time.sleep(1)

# 🎯 Show menu and take action
def show_menu():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📌 Prince's Terminal To-Do App")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Complete Task")
    print("4️⃣ Delete Task")
    print("5️⃣ Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# 🚀 Main loop
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("📥 Choose (1-5): ").strip()

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\n💾 Saving your tasks...")
            time.sleep(1)
            print("👋 Thanks for using the app, bud! Stay productive and have a great day!🎀🌷\n")
            break
        else:
            print("❌ Invalid choice. Try again.\n")
        time.sleep(1)

# 🧠 Run it!
if __name__ == "__main__":
    main()

# 📝 End of Prince's To-Do App
# 🏁 Thank you for using Prince's To-Do App! 🎉

