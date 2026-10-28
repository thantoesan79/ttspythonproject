import os;
import csv;


class Contact:
    def __init__(self,name,phone,email):
        self.name = name;
        self.phone = phone;
        self.email = email;

    def display(self):
        print(f"Name : {self.name}");
        print(f"Name : {self.phone}");
        print(f"Name : {self.email}");
        print("-"*30);


class ContactBook:
      def __init__(self,contactname = 'contact.csv'):
           self.contacts = [];
           self.contactname = contactname;
           self.ensure_csv_exists();
      
      def ensure_csv_exists(self):
           if not os.path.exists(self.contactname):
                with open(self.contactname,mode='w',newline='') as file:
                      writer = csv.writer(file);
                      writer.writerow(["Name","Phone","Email"]);
      
      def add_info(self,name,phone,email):
           newcontact = Contact(name,phone,email);
           self.contacts.append(newcontact);
           self.save_contact_to_csv(newcontact);
           
      def save_contact_to_csv(self,contact):
         try:
            with open(self.contactname,mode='a',newline='') as file:
                 wrtier = csv.writer(file);
                 wrtier.writerow([contact.name,contact.phone,contact.email]);
            print("Contact Save to CSV");
         except Exception as e:
              print(f"Error Saving contact to CSV: {e}");

      def view_contact(self):
           if not self.contacts:
                print("\n No contacts to display");
           else :
                print("\n All Contacts : ");
                for contact in self.contacts:
                     contact.display();

      def search_contact(self,search_name):
           print(f"\n Serarching for : {search_name}");
           found = False;
           for contact in self.contacts:
                if contact.name.lower() == search_name.lower():
                    contact.display();
                    found =True;
           if not found:
                print("\n Contact not found");
   
      def delete_contact(self,name_to_delete):
           removed = False;
           for contact in self.contacts[:]:#shallow copy;
                if contact.name.lower() == name_to_delete.lower():
                     self.contacts.remove(contact);
                     removed = True;
                     break;
           if removed:
                try:
                     with open(self.contactname,mode='w',newline='',encoding='utf-8')as file:
                          writer = csv.writer(file);
                          writer.writerow(["Name","Phone","Email"]);
                          for contact in self.contacts:
                               writer.writerow([contact.name,contact.phone,contact.email]);
                     print(f"{name_to_delete} has deleted");
                except Exception as e:
                     print(f"Error updating csv : {e}");
           else :
                print("Contact not found to delete");

      def load_from_csv(self):
           try:
              with open(self.contactname,mode='r',newline='',encoding='utf-8')as file:
                reader =csv.DictReader(file);
                for row in reader:
                     name = row["Name"];
                     phone = row["Phone"];
                     email = row["Email"];
                     self.contacts.append(Contact(name,phone,email));
              print(f"\n Contacts Loaded from {self.contactname}");
           except Exception as e:
                   print(f'Error loading from CSV : {e}');
         
        
#Main Menu;
 
def main():
     book =ContactBook();
     book.load_from_csv();
     print("Welcome to Contact Book Manager");
     while True:
          print('\n Menu: ');
          print("1. Add Contact");
          print("2. View All Contact");
          print("3. Search Contact");
          print("4. Delete Contact");
          print("5. Exit");
          choice = input("Enter your choice (1-5): ");

          if choice == '1':
               name = input("Enter name: ");
               phone = input("Enter phone number: ");
               email = input("Enter email: ");
               book.add_info(name,phone,email);
          
          elif choice == '2':
               book.view_contact();
          
          elif choice =='3':
               search_name = input("Enter the name you want to search : ");
               book.search_contact(search_name);
          
          elif choice == '4':
               delete_name = input("Enter a name that you want to Delete : ");
               book.delete_contact(delete_name);
          
          elif choice == '5':
               print('Good Bye');
               break;
          else:
               print("Invalid Choice. Please Enter a number from 1 to 5 :");
     
           
if __name__ == "__main__":
     main();