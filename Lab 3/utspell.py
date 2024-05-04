# This code implements a BASIC version of utspell that is found in the Unix program.
# It takes in an input word from the user and then returns to the user if the word is
# spelt correctly or incorrectly.

# Taking in user input on the word to be checked
print('Enter the word you would like to be spell-checked:')
word = input()

# If the word is found in the open dictionary file, we tell the user it is spelt correctly.
if word in open("/usr/share/dict/words").read():
    print("The word has been spelled correctly.")

# If the word is not found in the file, we tell the user it is spelt incorrectly. 
else:
    print("The word has been spelled incorrectly.")