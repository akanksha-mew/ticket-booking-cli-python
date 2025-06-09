import os
list = list(range(1, 51))
while True:
    os.system("cls")
    print(" MAIN MENU ".center(50, '*'))
    print('-' * 50)
    print("Select Options : \n[1] Check Available Seats \n[2] Book Ticket \n[3] Cancel Ticket")
    print('-' * 50)

    option = int(input("Enter your Option : "))
    print('-' * 50)

    if option == 1:
        for i in list:
            if i == "B":
                Ind = list.index(i)
                if (Ind+1) % 10 == 0:
                    print(i)
                else:
                    print(i, end="\t" )
            elif i % 10 == 0:
                print(i)
            else:
                print(i, end="\t")

    elif option == 2:
        S_No = int(input("Enter Seat number to Book : "))
        if list[S_No - 1] == "B":
            print("Seat is Already Booked !")
        else:
            Ind = list.index(S_No)
            list[Ind] = "B"
            print("Seat Booked Successfully")

    elif option == 3:
        S_No = int(input("Enter Seat number to Cancel : "))
        if list[S_No - 1] == "B":
            list[S_No - 1] = S_No
            print("Seat Cancelled Successfully!")
        else:
            print("Seat NOT Booked")

    else:
        print("Invalid Input")

    print('-' * 50)
    print("\nSelect Options : \n[1] Menu \n[2] Exit")
    print('-' * 50)
    choice = int(input("\nEnter your Option : "))

    if choice == 1:
        continue
    elif choice == 2:
        print("Exit !")
        exit(0)
    else:
        print("Invalid Choice")
        exit(0)
