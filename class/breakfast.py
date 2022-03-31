import time


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
            print_pause("Sorry, I don't understand. \n")
    return response


def intro():
    print_pause("Hello, I'm Bill the Breakfast Bot\n")
    print_pause("This morning we have two breakfast\n")
    print_pause("Options available are waffles with strawberry sauce\n")
    print_pause("or pancakes with honey butter.\n")

def get_order():  
    order = valid_input("Please place your order. "
                        "Would you like pancakes or waffles? \n\n",
                        "waffles", "pancakes")
    if "waffles" in order:
        print_pause("Waffles it is!")
    elif "pancakes" in order:
        print_pause("Pancakes it is")
    print_pause("Your order will be ready shortly.")
    order_again()

def order_again():
    order_again = valid_input("Would you like to order again?"
                              "Please say yes or no.\n",
                              "yes", "no")
    if "no" in order_again:
        print_pause("Okay! Thank you!")
    elif "yes" in order_again:
        print_pause("Okay, I'm glad to take another order\n")
        get_order()
    
def order_breakfast():
    intro()
    get_order()


order_breakfast()
