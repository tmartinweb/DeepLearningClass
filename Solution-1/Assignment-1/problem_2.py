

def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 2: \n")

    # Message prompts for user input
    message_1 = "Please enter a real number: "
    message_2 = "Please enter another real number: "
    message_3 = "User input was not a real number. Please try again..."

    while True:
        # Grab input from user
        x = input(message_1)
        try:
            # Attempt to cast to int
            x = int(x)
            # If no error, break out of while loop
            break
        except ValueError:
            # If we raise an error while attempting to cast into int
            try:
                # Attempt to cast to float
                x = float(x)
                # If no error, break out of while loop
                break
            except ValueError:
                # If both casts (to int and to float) raise an error, then the input is not valid
                print(message_3)

    while True:
        # Grab input from user
        y = input(message_2)
        try:
            # Attempt to cast to int
            y = int(y)
            # If no error, break out of while loop
            break
        except ValueError:
            # If we raise an error while attempting to cast into int
            try:
                # Attempt to cast to float
                y = float(y)
                # If no error, break out of while loop
                break
            except ValueError:
                # If both casts (to int and to float) raise an error, then the input is not valid
                print(message_3)

    # Produces output to console for addition, multiplication, raising by power, and floor division
    print("Output: \n")
    print(f"1. {x} added to {y} = {x + y}")
    print(f"2. {x} multiplied by {y} = {x * y}")
    print(f"3. {x} to the power of {y} = {x ** y}")
    print(f"4. The floor of {x} divided by {y} = {x // y}")
    print()
