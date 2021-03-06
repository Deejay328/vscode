import time

def print_pause(message):
    print(message)
    time.sleep(1)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")

    
def first_floor(items):
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
        ride_elevator(items)  
            

def second_floor(items):
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                        "in the human resources department.")
    if "ID card" in items:
        print_pause("The humans resources secretary greets you. "
                    "Upon seeing your ID card she hands you "
                    "your employee handbook.\n"
                    "You return to the elevator")
        items.append("Employee handbook")
        ride_elevator(items) 
    elif "Employee handbook" in items:
        print_pause("The HR folks are busy at their desks."
                    "There doesn't seem to be much to do here.\n"
                    "You return to the elevator.")
        ride_elevator(items)
    else:
        print_pause("After arriving to the second floor "
                    "a security guard turns you around "
                    "because you do not have an ID card\n"
                    "You return to the elevator") 
        ride_elevator(items)


def third_floor(items):
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    if "Employee handbook" in items:
            print_pause("You use your Id card to unlock the door and enter your office.\n"
                        "You sit down and begin reading you Employee handbook.") 
    elif "Id card" in items:
        print_pause("You use your Id card to gain access to the engineering department\n"
                     "You are unsure how to log into you computer.\n"
                     "Maybe an employee handbook would help\n"
                     "You return to the elevator")
        ride_elevator(items)
    else:
        print_pause("You exit the elevator but cannot access the "
                    "engineering department without an Id card\n"
                    "You return to the elevator.")
        ride_elevator(items)
            
           
def ride_elevator(items):
    print_pause("Please enter the number " 
                "for the floor you would "
                "like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor(items)        
    elif floor == '2':
        second_floor(items)                  
    elif floor == '3':
        third_floor(items)
        

def play_game():
    items = []
    intro()
    ride_elevator(items)


play_game()