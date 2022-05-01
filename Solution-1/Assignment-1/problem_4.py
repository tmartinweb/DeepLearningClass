

def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 4: \n")

    # Conversion Constant
    lbs_to_kg = 0.453592

    # Message prompts for user input
    message_1 = "Please enter the number of student weights would you like to compute: "
    message_2 = "Enter the #{} student's weight (in lbs.): "
    message_3 = "User input was not a whole number. Please try again..."
    message_4 = "User input was not a real number. Please try again..."

    while True:
        try:
            # Attempt to cast user input directly to int
            num_students = int(input(message_1))
            # If no error, break out of while loop
            break
        except ValueError:
            # If cast to int raises an error, then the input is not valid
            print(message_3)

    # Declare list into which we will put the students' weights as input from user
    raw_list = []
    while True:
        try:
            # Grab input from user, directly casting it to float
            # NOTE: by using range(len(raw_list), we will initially start at 0,
            #   but if we error on an input, we only have to redo that input, and continue from there
            for index in range(len(raw_list), num_students):
                raw_list.append(float(input(message_2.format(index + 1))))
            # If no error, break out of while loop
            break
        except ValueError:
            # If cast to float raises an error, then the last input is not valid
            print(message_4)

    # Declare list for looped calculation
    looped_list = []
    # For each weight in the raw_list
    for weight in raw_list:
        # Append each weight after converting lbs to kg and rounding to 2 decimal places
        looped_list.append(round(weight * lbs_to_kg, 2))

    # Output looped list to console
    print("\nLooped list: ")
    print(*looped_list, sep=", ")
    print()

    # Declare and define list for comprehension calculation
    # For each weight in raw_list, convert from lbs to kg, then round to 2 decimal places
    comprehension_list = [round(weight * lbs_to_kg, 2) for weight in raw_list]

    # Output comprehension list to console
    print("Comprehension list: ")
    print(*comprehension_list, sep=", ")
    print()
