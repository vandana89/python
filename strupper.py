# Read input string from the user
string = input("Enter a string: ")

# Split the string into words
words = string.split()

# Check if there is at least a second word
if len(words) > 1:
    # Extract the second word and convert it to uppercase
    second_word_upper = words[1].upper()
    print("Second word in uppercase:", second_word_upper)
else:
    print("The input string does not contain a second word.")
