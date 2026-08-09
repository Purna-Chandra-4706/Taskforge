

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

if __name__ =="__main__":
        list_tasks()


