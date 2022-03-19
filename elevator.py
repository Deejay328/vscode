import time
items = []

def print_pause(message):
    print(message)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number" 
                "for the floor you would"
                "like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID "
                        "card.")
            items.append("ID card")
            print_pause("You return to the elevator")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
        if "ID card" in items:
            print_pause("The humans resources secretary greets you"
                        "Upon seeing your ID card she hands you"
                        "your employee handbook\n"
                        "You return to the elevator")
            items.append("Employee handbook") 
        elif "Employee handbook" in items:
            print_pause("The HR folks are busy at their desks."
                        "There doesn't seem to be much to do here.\n"
                        "You return to the elevator")
        else:
            print_pause("After arriving to the second floor"
                        "a security guard turns you around"
                        "because you do not have an ID card\n"
                        "You return to the elevator")           
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")
        if "Id card" and "Employee handbook" in items:
            print_pause("You use your Id card to unlock the door and enter your office.\n")
    print_pause("Where would you like to go next?")
