import os;
from datetime import datetime;

TASK_FILE = "task.txt";
#creating task file

def load_tasks():
    tasks=[];
    #task need to check task box
    if os.path.exists(TASK_FILE):
    #to check if the file is exist 
        with open(TASK_FILE,mode="r",encoding="utf-8") as file:
            for line in file:
            #line contain each sentences one at a time 
                task,timestamp,priority = line.strip().split("||");
                priority = int(priority)
                tasks.append({"task":task,"timestamp":timestamp,"priority":priority});
    return tasks;

def save_task(tasks):
    with open(TASK_FILE,mode='w',encoding="utf-8") as file:
        for t in tasks:
            file.write(f"{t["task"]}||{t["timestamp"]}|| {t["priority"]} \n");


def  view_task(tasks):
    if not tasks:
        print("No task is available");
        return;
    sorted_task = sorted(tasks,key=lambda x:x["priority"]);
    print("\n Your tasks : ")
    for i,k in enumerate(sorted_task,1):
        print(f"{i}. {k['task']} (Priority : {k['priority']}, Added : {k['timestamp']})");



def add_task(tasks):
    task = input("Enter Task :");
    priority = int(input("Enter Pirority (1=High,2=Medium,3=low) : "));
    timestamp = datetime.now().strftime("%y-%m-%d %H-%M-%S");
    tasks.append({"task":task,"timestamp":timestamp,"priority":priority});
    save_task(tasks);
    print("All Task are Added");



def delete_tasks(tasks):
    view_task(tasks);
    
    try:
        choice = int(input("Choose a number you want to Delete : "));
        if 0<choice<=len(tasks):
          remove = tasks.pop(choice-1);
          save_task(tasks);
          print(f" Delete the {remove['task']}");
    
    except ValueError:
        print("Please enter a valid number ")

def main():
   tasks =  load_tasks();
   while True:
       print("\n TO-DO-LIST MANAGER");
       print("1. Add Task \n2. View Task\n3. Delete Task\n4. Exist");
       option =input("Enter an option : ");
       if option == '1':
           add_task(tasks);
       elif option == '2':
           view_task(tasks);
       elif option == '3':
           delete_tasks(tasks);
       elif option == '4':
           print("Good Bye");
           break;
       else:
           print("Invalid option.Try again");


if __name__ =="__main__":
    main();
