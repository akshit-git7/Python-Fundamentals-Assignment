
def calculator():
        
    print("Select one operation:")
    print("1. Addition:")
    print("2. Subtraction:")
    print("3. Multiplication:")
    print("4. Division:")

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mult(a,b):
        return a*b
    def div(a,b):
        return a/b
    while True:
            choice = input("Enter choice (1/2/3/4) or 'exit' to quit: ")
            
            if choice.lower() == 'exit':
                print("Exiting the calculator.")
                break
            
            if choice in ['1', '2', '3', '4']:
                    n1 = float(input("Enter first number: "))
                    n2 = float(input("Enter second number: "))
                    
                    if choice == '1':
                        print(f"Result: {add(n1, n2)}")
                    elif choice == '2':
                        print(f"Result: {sub(n1, n2)}")
                    elif choice == '3':
                        print(f"Result: {mult(n1, n2)}")
                    elif choice == '4':
                        print(f"Result: {div(n1, n2)}")
            else:
                print("Invalid choice. Please select a valid operation.")
calculator()
