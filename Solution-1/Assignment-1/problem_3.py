

def solution(line_break):
    # Print line_break and problem number to console
    print(line_break + "Problem 3: \n")

    # Declare and define dictionary of words to search for and their replacements
    word_dict = {"python": "pythons", "Python": "Pythons"}

    # Message prompt for user input
    message = "Enter a sentence: "

    # Grab input from user
    output = input(message)

    # For each entry in the dictionary of search words
    for word, replacement in word_dict.items():
        # Use str.replace() to find and replace all instances of keywords
        output = output.replace(word, replacement)

    # Output result to console
    print("Output: " + output)
    print()
