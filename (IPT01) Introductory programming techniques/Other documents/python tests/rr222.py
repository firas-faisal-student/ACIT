while True:
    response = input("Enter a number (or 'q' to quit): ")
    
    if response.lower() == 'q':
        print("Exiting the program.")
        break
    
    try:
        number = int(response)
        remainder = number % 2
        if remainder == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")