# python programming task
# the aim of this task is to dtermine our abilities to create alternate and manipulate characters and words in a string
# range, input, len, upper and lower, and split functions were used.
# for loop, if and else statements were used.

main_string = input("Please enter a sentence: ") # user makes an input
    
    # Alternate characters
alt_string = '' #blank string to store the string with alternate characters capital and small
for i in range(len(main_string)): #loop to convert the letters to upper case and lower case
    if i % 2 == 0:
        alt_string += main_string[i].upper() # converts the characters at the odd index to uppercase using the upper() method
    else:
        alt_string += main_string[i].lower() # converts the remaining characters to lower case
print("Alternate characters:", alt_string) # prints out a sentence containing words with alternating uppercase and lower case letters

print(" ") # empty string to create space

    # Alternate words
main_string2 = main_string.split() #breaks down a string into a list of different words
alt_string2 = '' #blank string to store the string with alternate words capital and small
for i in range(len(main_string2)): #loop to convert the letters to upper case and lower case
    if i % 2 == 0:
        alt_string2 += main_string2[i].lower() #converts the words at the odd index to uppercase using the upper() method
    else:
        alt_string2 += main_string2[i].upper() #converts the remaining words to lower case
    if i != len(main_string2): # if statement to add space in between words
        alt_string2 += ' '  # Add space between words
print("Alternate words:", alt_string2) #prints out a sentence with alternating uppercase and lower case words
