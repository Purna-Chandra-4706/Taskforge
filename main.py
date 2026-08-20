
"""Taskforge - A powerful CLI task manager for productivity."""

tasks = [
    "Wake Up",
    "Drink Water",
    "Eat Breakfast",
    "Go To lab",
    "Commute to hostel"

]

def search_task(keyword):

     

     flag = False
     for task in tasks:
          if(keyword.lower() in task.lower()):
               print(f"{task} is matching the {keyword} keyword\n")
               flag = True;

     if(flag==False):
          print(f"No task found matching {keyword}\n")
        
     

def list_tasks():
    """Print each task in the last with numbered Index."""
    print("Your Tasks:\n")
    for index, task in enumerate(tasks,start=1):
        print(f"{index}. {task}\n")

def add_tasks(task_name):
     """Add a new task"""
     tasks.append(task_name)
     print(f"Task Added: {task_name}\n")

def remove_task(task_number):
     """Delete a task"""
     if(1<=task_number<=len(tasks)):
          print(f"Deleted Task: {tasks[task_number-1]}\n")
          tasks.pop(task_number-1)
     else:
          print(f"Error: The task number does not exist\nEnter in between 1 and {len(tasks)}\n")
          
def count_tasks():

    if(len(tasks)==0):
        print("You have no tasks\n")
    elif(len(tasks)==1):
        print("You have 1 task\n")
    else:
        print(f"You have {len(tasks)} tasks\n") 

def clear_tasks():

     if(len(tasks)==0):
          print("No tasks to clear\n")
     else:
          print("All tasks cleared!\n")
          tasks.clear()
         


def show_help():

     print(f"\n===Menu===\n")
     print("Choice 1: List the all tasks present\n")
     print("Choice 2: Add a task to present tasks\n")
     print("Choice 3: Remove a task from tasks\n")
     print("Choice 4: Count number of tasks\n")
     print("Choice 5: Search a task from tasks\n")
     print("Choice 6: Clear all tasks")
     print("Choice 7: Helper to the user\n")
     print("Choice 8: Exit\n")
         
         
     

found = True



while(found):
        print("=== TaskForge ===\n")
        print("Welcome to TaskForge! Manage your tasks efficiently.\n")
        print("1.List tasks\n")
        print("2.Add task\n")
        print("3.Remove Task\n")
        print("4.Count Task\n")
        print("5.Search Task\n")
        print("6.Clear Tasks\n")
        print("7.Show Menu\n")
        print("8.Exit\n")
        try:
          n = int(input("Choose an option: "))
          print("\n")
        except:
           print("\nPlease enter a valid number!\n")
           continue
           

        match n:
             case 1:
                   list_tasks()
             case 2:
                   add_tasks(input("Enter a task: "))
             case 3:
                  remove_task(int(input("Enter a task number to delete: ")))
             case 4:
                  count_tasks()
             case 5:
                  search_task(input("Enter the keyword: "))
             case 6:
                  clear_tasks()
             case 7:
                  show_help()
             case 8:
                  print("Exiting....\n")
                  found = False
             case _:
                  print("Enter a Valid choice\n") 
                
                  
                  
                  

        
       
        
        
        
        
       


