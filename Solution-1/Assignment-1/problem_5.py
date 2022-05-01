
# Precondition: input is a non-empty string
def string_alternative(input_string):
    # Return a string of every other member of the input string using string splicing
    return input_string[::2]


def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 5: \n")

    # Message prompts for user input
    message_1 = "Enter a string input: "
    message_2 = "User input invalid. Please re-enter a valid string input: "

    # Grab input from user
    user_input = input(message_1)

    # Ensure input is not empty
    while not len(user_input):
        user_input = input(message_2)

    # Output string from a call to user-defined function 'string_alternative' to console
    print("Output: " + string_alternative(user_input))
    print()
