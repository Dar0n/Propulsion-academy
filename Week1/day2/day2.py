"""
This is a file with exercises for the day 2 from Full-Stack program at Propulsion Academy
"""

# Exercise 1.1
# Even numbers

def only_even(lst):
    return list(filter(lambda a : a % 2 == 0, lst))

print("Exercise 1")
print(only_even([1,2,3,4,5,6,7,8,9,10]))



# Exercise 1.2
# Square elements

def square_list(lst):
    return list(map(lambda x: x*x , lst))

print("")
print("Exercise 2")
print(square_list([1,2,3,4,5,6,7,8,9,10]))



# Exercise 1.3
#Squared even numbers

def square_even(lst):
    return square_list(only_even(lst))

print("")
print("Exercise 3")
print(square_even([1,2,3,4,5,6,7,8,9,10]))


# Exercise 1.4
# Find certain numbers

# First realization using for loops without using map or filter

def find_numbers_lame(min,max):
    for i in range(min, max+1):
        if i % 7 == 0 and i % 5 != 0:
            yield i

print("")
print("Exercise 4: lame version")
print(list(find_numbers_lame(1,50)))

# Second realization with using filter

def find_numbers_cool(min, max):
    return list(filter(lambda x: x % 7 == 0 and x % 5 != 0, list(range(min,max))))

print("")
print("Exercise 4: cool version")
print(list(find_numbers_cool(1,50)))


# Exercise 2.
# Webstore

# First realization - with for loop without map

def compute_totals_lame(orders):
    for order in orders:
        subtotal = order["quantity"]*order["price_per_item"]
        if subtotal < 100:
            yield (order["id"], subtotal + 10)
        else:
            yield (order["id"], subtotal)

orders = [
  {
    'id': 'order_001',
    'item': 'Introduction to Python',
    'quantity': 1,
    'price_per_item': 32
  },
  {
    'id': 'order_002',
    'item': 'Advanced Python',
    'quantity': 3,
    'price_per_item': 40

  },
  {
    'id': 'order_003',
    'item': 'Python web frameworks',
    'quantity': 2,
    'price_per_item': 51
  }
]

print("")
print("Exercise Webstore - lame version")
totals = compute_totals_lame(orders)
print(list(totals))
# result is [('order_001', 42), ('order_002', 120), ('order_003', 102)]

# Second realization - with map

def compute_totals_cool(orders):
    return list(map(lambda order: (order["id"],order["quantity"]*order["price_per_item"]) \
        if order["quantity"]*order["price_per_item"] > 100 \
        else (order["id"],order["quantity"]*order["price_per_item"] + 10), orders))

print("")
print("Exercise Webstore - cool version")
print(compute_totals_cool(orders))


# Third realization - map without lambda

def add_10_franks(order):
    subtotal = order["quantity"]*order["price_per_item"]
    if subtotal < 100:
        return (order["id"], subtotal + 10)
    else:
        return (order["id"], subtotal)

def compute_totals_supercool(orders):
    return list(map(add_10_franks, orders))

print("")
print("Exercise Webstore - supercool version")
print(compute_totals_supercool(orders))


# Exercise 3
# Iinput and range

# Version without map

def generate_dictionary_lame(n):
    lst = [n for n in range(1,n+1)]
    result = {}
    for i in lst:
        result[i] = i*i
    return result


print("")
print("Exercise 3 - input and range")
print(generate_dictionary_lame(5))


# Version with map

def generate_dictionary_cool(n):
    return {i:i*i for i in range(1,n+1)}


print("")
print("Exercise 3 - input and range")
print(generate_dictionary_cool(7))


# Exercise 4
# List comprehensions

def last_5_squares():
    return [i*i for i in range(1,21)][-5:]

print("")
print("Exercise 4 - list comprehensions")
print(last_5_squares())


# Exercise 5
# Print stye

def print_style():
    for i in range(1,11):
        if i % 2 == 0:
            print(i, end = ""),
        else:
            print("_", end = ""),
    print("") # Just to add new line so that next print would be at least on the next line

print_style()


# Esxecise 6
# BMI calculator

def get_BMI():
    print("Let's calculate your BMI (kg/m^2)")
    weight = float(input("What is your mass in KG?\n"))
    height = float(input("What is your height in CM?\n"))/100
    bmi = weight/(height*height)
    if bmi < 18.5:
        print("You are underweight, please go and eat something!")
    elif bmi < 25:
        print("Your weight is absoutely normal, you are doing great")
    else:
        print("Man, you are overweight! Put that pizza down and go to the gym!")
    return round(bmi, 1)

print("")
print("")
#print(get_BMI())


#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
# Exercise 7
# Shopping list

def shopping_list():

    shop_list = []

    # Function to display help

    def help_menu():
        print("Press 'h' for help menu")
        print("Press 's' to show the items in your list")
        print("Press 'a' add a new item to the list")
        print("Press 'r' to remove an item from the list")
        print("Press 'q' to quit\n")

    # Function which displays current shopping list to the user

    def show_items():
        if not shop_list:
            print("There are no items on the list!")
        else:
            for i in range(len(shop_list)):
                print("{}: {}".format(i+1,shop_list[i]))

    # Function that adds an item to the shopping list

    def add_item():
        item_to_add = input("What would you like to add?\n")
        if item_to_add: # if the line is not empty...
            shop_list.append(item_to_add)
        else:
            print("You tried to enter empty line, try again!")
            add_item()

    # Function to remove an item from the list if present

    def remove_item():
        item_to_remove = input("What item would you like to remove?\n")
        if item_to_remove: # if the line is not empty...
            if item_to_remove in shop_list:
                shop_list.remove(item_to_remove)
                print("{} is removed from the list".format(item_to_remove))
            else:
                print("There is no {} in your list. Please double check".format(item_to_remove))
                remove_item()
        else:
            print("You tried to enter empty line, try again!")
            remove_item()

    # Display help menu for the first time so user knows what he can do
    help_menu()

    while True:

        user_input = input("What do you want to do?\n")
        if user_input == "h":
            help_menu()
        elif user_input == "s":
            show_items()
        elif user_input == "a":
            add_item()
        elif user_input == "r":
            remove_item()
        elif user_input == "q":
            print("Thank you for shopping, see you next time!")
            break
        else:
            print("Unauthorised action, please follow the help guide or contact administrator")




print("")
print("Exercise 7 - shopping list")
print("")
# print(shopping_list())

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################

# Exercise 8
# Number guess game

from random import randint

def start():

    # Generating random number

    number_to_guess = randint(1,10)

    # Function to check user guess
    def check_user_guess(guess, num_of_guesses):
        if guess == number_to_guess:
            print("Congratulations! You guessed it! It took you {} attempts".format(num_of_guesses))
            return True
        elif guess > number_to_guess:
            print("Nope! It's lower than {}. ".format(guess), end = "")
            if num_of_guesses == 5:
                print("\n")
            else:
                print("Try again!")
        else:
            print("Nope! It's higher than {}. ".format(guess), end = "")
            if num_of_guesses == 5:
                print("\n")
            else:
                print("Try again!")

    # function to play again
    def play_again():
        want_to_play = input("Do you wan to play again? Press 'y' for Yes, press 'n' for No\n")
        if want_to_play == "y":
            start()
        elif want_to_play == "n":
            print("Thanks for the game! See you next time!")
        else:
            print("I didn't get you, looks like you mistyped. Could you repeat that again?\n")
            play_again()

    # Body of the main function

    print("I am thinking of a number from 1-10. Can you find it? You have 5 tries. (Shhhhhh - it's actually {})".format(number_to_guess))
    count = 0
    while True:
        user_guess = input("Guess what it is:\n")
        try:
            user_guess = int(user_guess)
            count += 1
            # check_user_guess(user_guess, count)
            if(check_user_guess(user_guess, count)):
                break
            if count == 5:
                print("Sorry, that was your last attempp. The number was {}".format(number_to_guess))
                break

        except ValueError:
            print("You entered not a number, please try again.\n")

    play_again()







print("")
print("Exercise 8 - guess game")
# start()


def hangman():

    # Initiating array to store words from the text file
    words = []

    # Array to store letters that were tried by user
    tried_letter = []

    # Line that is printed to user while he is guessing
    current_guess={"line": ""}

    # Opening the file, reading it line by line and adding each line i.e. each word to the array
    file = open("words_list.txt", 'r')
    for line in file:
        words.append(line)

    # Generating random number to get random word from our list of words

    word_to_guess_number = randint(1,len(words))
    word_to_guess = words[word_to_guess_number][:-1]
    print("The word is {}".format(word_to_guess))

    # Filling current line with empty underscores at the beginning
    for i in range(len(word_to_guess)):
                current_guess["line"] = current_guess["line"] + "_ "


    # Function to change the current line - replacing underscores with correct letter

    def build_current_guess(letter):
        guess_lst = list(current_guess["line"])

        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter:
                if i == 0:
                    guess_lst[i] = letter
                else:
                    guess_lst[2*i] = letter
        current_guess["line"] = "".join(guess_lst)
        return current_guess["line"]


    # Function to check if the user wants to play again
    def play_again():
        want_to_play = input("Do you wan to play again? Press 'y' for Yes, press 'n' for No\n")
        if want_to_play == "y":
            hangman()
        elif want_to_play == "n":
            print("Thanks for the game! See you next time!")
        else:
            print("I didn't get you, looks like you mistyped. Could you repeat that again?\n")
            play_again()

    # Function to check if the letter was already check before

    def is_already_there(letter):
        return letter in tried_letter

    def guess_word():
        # Number of wrong attempts from user
        count = 0
        print("To quit the game simply type 'quit'\nYou only have 7 tries for this game")
        while count < 7:
            print(current_guess["line"])
            print("You have {}/7 tries left".format(count))
            user_input = input("\nPlease enter letter (or quit)\n")
            # Check if user wants to quit
            if user_input == "quit":
                return 0
            # If user entered only one letter..
            if len(user_input) == 1 and user_input.isalpha():
                # If the letter was entered before..
                if is_already_there(user_input):
                    print("You already tried this one!")
                # If the letter is new..
                else:
                    tried_letter.append(user_input)
                    if user_input in word_to_guess:
                        build_current_guess(user_input)
                        if "_" not in current_guess["line"]:
                            print("You won!")
                            break
                    else:
                        print("Wrong letter")
                        count += 1
            # If the user made incorrect input
            else:
                print("Please enter only one letter")
        if count == 7:
            print("Sorry, you lost.")
        play_again()
    guess_word()



print("")
print("")
print("Exercise 9 - Hangman")
hangman()
