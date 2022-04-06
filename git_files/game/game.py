from logging import raiseExceptions
import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please enter a valid response \n")
    return response


def start():
    items = []
    print_pause("You are an adventurer setting out "
                "to rid a town of an evil witch. ")
    print_pause("Leaving the safety of the town gates "
                "you see before you fields of grain, "
                "glowing in the early morning light. ")
    print_pause("To your right a river flows, forming a natural barrier.")
    print_pause("To your left stands a forest of considerable size.")
    town_1(items)


def town_1(items):
    print_pause("Your path splits in front of you. "
                "The path on the right follows along the river; "
                "the left leads into the woods. ")
    choice = valid_input("Please choose a path by typing:\n"
                         "Right\nLeft\n",
                         "right",
                         "left")
    if "right" in choice:
        river(items)
    elif "left" in choice:
        forest(items)


def river(items):
    print_pause("You head towards the river, following the path "
                "beside it until you eventually "
                "run into a goblin.")
    if "amulet" in items:
        print_pause("The goblin is still bitter to have lost his amulet, "
                    "you decide not to approach him. "
                    "You head back towards the town.")
        town_1(items)
    else:
        print_pause("You ask the goblin if he knows anything "
                    "about the witch in the area.")
        print_pause("A grin crosses his face as he tells you he "
                    "has an amulet that makes the wearer immune "
                    "to the witches magic.")
        print_pause("He offers to sell you the amulet for 1,000 gold pieces. "
                    "You have no gold so you "
                    "must ask the golblin for another option.")
        print_pause("Pulling two die out of his pocket, he offers a game. "
                    "Whomever rolls highest nummber wins.")
        print_pause("If you win, the amulet is yours. If the goblin wins, "
                    "you must serve him forever. ")
        play_dice = valid_input("Would you like to take the goblin's bet?\n"
                                "Please enter yes or no\n",
                                "yes",
                                "no")
        if "yes" in play_dice:
            (dice_game(items))
        elif "no" in play_dice:
            print_pause("You turn back towards town")
            town_1(items)


def forest(items):
    print_pause("You head into the forest")
    print_pause("You hear a loud shreik. It's the witch!")
    if "amulet" in items:
        print_pause("The witch tries to use her magic on you "
                    "but it has no effect.")
        print_pause("Seeing your immunity to her powers, the witch flees.")
        print_pause("Congratulations! You defeated the witch!")
        play_again()
    else:
        print_pause("As the witch's spell starts to take it's toll "
                    "you start to feel light headed.")
        print_pause("Your vision starts to turn dark and you feel youself"
                    "fading out of conscienousness")
        print_pause("GAME OVER-YOU HAVE DIED")
        play_again()


def play_again():
    play_again = valid_input("Would you like to play again?\n"
                             "Enter \"yes\" or \"no\"\n",
                             "yes",
                             "no")
    if "yes" in play_again:
        print_pause("Okay! Good luck!")
        start()
    elif "no" in play_again:
        print_pause("Understood, thanks for playing!")


def dice_game(items):
    hero_roll = random.randint(1, 6)
    goblin_roll = random.randint(1, 4)
    print_pause("You take the challenge and go first "
                "you roll a ")
    print(hero_roll)
    print_pause("The goblin looks menacingly at you and takes his turn "
                "he rolls a ")
    print(goblin_roll)
    if (hero_roll) > (goblin_roll):
        print_pause("You win and gain the magic amulet."
                    "You hurry back to town before "
                    "he can protest.")
        items.append("amulet")
        town_1(items)
    elif hero_roll == goblin_roll:
        print_pause("You tie and roll again")
        dice_game(items)
    else:
        print_pause("Oh no, the goblin won. You spend the rest"
                    "of your days serving him")
        print_pause("GAME OVER")
        play_again()


start()
