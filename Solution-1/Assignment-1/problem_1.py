import random


def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 1: \n")

    # Number of letters to delete, feel free to change
    num_letters_to_delete = 2

    # Message prompt for user input
    message = "Enter desired word(s): "

    # Grab input from user, instantiating a list in which to store input
    letters_list = list(input(message))

    # For as many letters as we wish to delete (Instructions say 2)
    for x in range(num_letters_to_delete):
        # If there is a member of letters_list (this ensures an IndexError doesn't happen for an empty list)
        if len(letters_list):
            # Pop a random index from letters_list
            letters_list.pop(random.randint(0, len(letters_list) - 1))

    # Join list to a string, then reverse string, then output to console
    print("Output: " + ''.join(letters_list)[::-1])
    print()
