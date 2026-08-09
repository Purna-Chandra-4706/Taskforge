

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

def remove_task(task_number):
     """Delete a task"""
     if(1<=task_number<=len(tasks)):
          print(f"Deleted Task: {tasks[task_number-1]}")
          tasks.pop(task_number-1)
     else:
          print(f"Error: The task number does not exist\nEnter in between 1 ans {len(tasks)}")
          
        
         
     


     

if __name__ =="__main__":
        
        add_tasks("Eat Lunch")
        add_tasks("Take Rest")
        remove_task(4)
        
        list_tasks()


