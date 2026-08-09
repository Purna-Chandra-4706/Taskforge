

tasks = [
    "Wake Up",
    "Drink Water",
    "Eat Breakfast",
    "Go To lab",
    "Commute to hostel"

]

def list_tasks():
    """Print each task in the last with numbered Index."""
    print("Your Tasks:")
    for index, task in enumerate(tasks,start=1):
        print(f"{index}. {task}")

def add_tasks(task_name):
     """Add a new task"""
     tasks.append(task_name)
     print(f"Task Added: {task_name}")


if __name__ =="__main__":
        add_tasks("Eat Lunch")
        add_tasks("Take Rest")
        list_tasks()


