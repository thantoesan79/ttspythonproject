import csv;
import os;

FileName = "budget_data.csv";
Categorties = ["Food","Transport","Rent","Utilities","Entertainment","Other"];

def intialize_csv():
    if not os.path.isfile(FileName):
        with open(FileName,mode="w",newline="") as file:
            wrtier = csv.writer(file);
            wrtier.writerow(["Categorties","Amount","Type"]);



def get_transition(trans_type):
    print(f"\n--Add{trans_type}--");
    print(f" Available Category : {','.join(Categorties)}");
    

    while True:
        category = input("Enter category: ").strip().capitalize();
        if category in Categorties:
            break;
        print(f"Invalid category .Please choose from the list of : {','.join(Categorties)}");


    while True:
        try:
            amount = float(input("Enter the amount : ")) ;
            if amount <= 0:
                print("Amount should be a positive number.")
                continue;
            break;
        except ValueError:
            print("Invalid input.Please enter a numeric value for amount");
    return category,amount,trans_type;

def save_data(category,amount,trans_type):
    with open(FileName,mode="a",newline='') as file:
        writer = csv.writer(file);
        writer.writerow([category,amount,trans_type]);
    print(" Transaction data is saved");
          

def  calculate_balance():
     if not os.path.isfile(FileName):
         return 0.0,0.0,0.0 ;
     income = 0.0;
     expense = 0.0;
     with open(FileName,mode="r") as file:
         reader =csv.DictReader(file);
         for row in reader:
             try: 
                amount = float(row["Amount"]);
                if row["Type"] == "Income":
                    income += amount;
                else:
                    expense += amount;
             except ValueError:
                 continue;
     return income,expense,income-expense;

def display_report():
    print("\n","="*30);
    print("     Budget Report");
    print("\n","="*30);
    income,expense,Balance = calculate_balance();
    print(f"Total income : $ {income :>10.2f}");
    print(f"Total Expense: ${expense:>10.2f}");
    print(f"Current Balance : $ {Balance :>10.2f}");
    print("="*30);
    

def Main():
     intialize_csv()  
     menu ={"1" : ("Add Income","Income"),
            "2" : ("Add Expense","Expense"),
            "3" : ("View Report",None),
            "4" : ("Exit",None)
            }
     while True:
           print("\n ------- Personal Budget Tracker -------");
           for k,v in menu.items():
               print(f"{k},{v[0]}");
           
           choice = input("Select an option(1-4) : ").strip()
               
           if choice in ["1","2"]:
                 data = get_transition(menu[choice][1]);
                 save_data(*data);
           elif choice in ["3"]:
                   display_report();
           elif  choice in ["4"]:
                   print("Goodbye Have a great day");
                   break;
           else :
                   print("Invalid choice . Try Again");
         
            
if __name__ == "__main__":
     Main();