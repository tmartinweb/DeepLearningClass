import re


def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 6: \n")

    # I decided to put a pause for the beginning of problem 6,
    # since it doesn't require user input, it's easy for the console to 'get ahead' of the user
    message = "Problem 6 does not ask for user input, please press any key to continue..."
    input(message)

    # Name (and path, if required) of file to process
    filename = "example_file.txt"
    # Declare dictionary to store words counted (key) and their counts (value)
    word_dict = {}

    # Open file to read with auto-close method
    with open(filename, 'r') as file:
        for line in file:
            # Discard all non-alphanumeric and non-whitespace characters
            scrubbed_line = re.sub(r"[^\w\s]", "", line)
            # Discard all new lines
            scrubbed_line = re.sub(r"\n", "", scrubbed_line)
            # Create list from splitting string
            words_in_line = scrubbed_line.split(" ")

            for word in words_in_line:
                # Modify for consistent key capitalization
                cap_word = word.lower().capitalize()
                # If the word is in the dictionary...
                if cap_word in word_dict:
                    # Add 1 to its count
                    word_dict[cap_word] = word_dict[cap_word] + 1
                else:
                    # Create a new key with count 1
                    word_dict[cap_word] = 1

    # Output word count to console
    print("Word_Count: ")
    print(word_dict)

    # Open file to append, with auto-close method
    with open(filename, 'a') as file:
        # Append heading to file
        file.write("\n\nWord_Count: \n")
        # For each key/value pair in dictionary...
        for key, count in word_dict.items():
            # Append word and count to file, line by line
            file.write(str(key + ": " + str(count)) + "\n")

    # Print status to console
    print("\nWord count appended to file.")
    print()

