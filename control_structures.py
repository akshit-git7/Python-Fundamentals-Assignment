def classification():
    while True:
        user = input("Enter a number (or 'exit' to quit): ")
        
        if user.lower() == "exit":
            print("Exiting")
            break
        number = float(user)
        if number > 0:
            print("Number is positive.")
        elif number < 0:
            print("Number is negative.")
        else:
            print("The number is zero.")

classification()