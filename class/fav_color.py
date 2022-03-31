def green_room():
    print("you're in the green room")


def blue_room():
    print("you are in the blue room.")


def choose_room():
    choice = input("Would you like to go into the green room"
                   "or the blue room?\n").lower()
    if choice == "green":
        green_room()
    elif choice == "blue":
        blue_room()
    else:
        print("I don't know what that is.")
        choose_room()

choose_room()

