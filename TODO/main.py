from todo import  add_tsk, view_tsk, del_tsk
from utils import clr_scr, user_inp

def main():
    while True:
        clr_scr()
        print("Select  an option:")
        print("1. Add ")
        print("2. Delete ")
        print("3. View ")
        print("4. Type 'exit' to close the program")
        choice = input("Enter choice (1/2/3 or 'exit') ")
        if choice.lower() == 'exit':
            print("Exited")
            break
                
        elif choice == '1':
            tsk = user_inp("Enter task:")
            add_tsk(tsk)
            user_inp("\nPress any key to return to the menu.")
                   
        elif choice == '2':
            view_tsk()
            try:
                i = int(user_inp("Enter the task index to delete: "))
                del_tsk(i)
            except:
                print("Invalid input. Please enter a number.")
            user_inp("\nPress any key to return to the menu.")

        elif choice == '3':
            view_tsk()
            user_inp("\nPress any key to return to the menu.")
        else:
            print("Invalid input.")

if __name__=="__main__":
    main()
           