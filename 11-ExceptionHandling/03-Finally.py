while True:
    try:    
        pin = int(input("Enter your pin : "))

        if pin == 1234:
            print("Welcome user")
        else:
            print("Try Again")

    except ValueError as v:
        print("Wrong Choice",v)

    finally:
        print("I will always execute")
