# Python programming Language
# the aim of this task is to read a DOB.txt file in your chosen directory and be able to produce its modified form in the output panel
# in that names are printed under a title called name and bithdates printed under the title called birthdates
# open(), readlines(), strip(), split(), join(), append() functions are used
# tools such as lists, slicing, for loop statements are used

# Read data from DOB.txt file
with open("DOB.txt", "r") as file: # locates and opens DOB.txt
    dob = file.readlines() # Reads data from DOB.txt file

# Extract names and birthdates
names = [] # opens an empty list called names
birthdates = [] # opens an empty list called birthdates
for line in dob: # loop for producing separate names and birthdates is created
    data = line.strip().split(' ') # an empty separator is created to ensure the names and birthdates appear differently.
    name = ' '.join(data[:-3])  # Join name parts and removes the birthdate parts
    birthdate = ' '.join(data[-3:])  # Join birthdate parts and removes the name parts
    names.append(name) # add name to the list of names
    birthdates.append(birthdate) # add date to the list of birthdates

# Print names section
print("\033[1m \nName \033[0m") # prints name in bold
# \033[ starts the escape sequence.
# 1 represents the code for making the text bold. changing 1m to 2m, returns to non-bold text, to 3m produces italics, 4m underlines text.
# m marks the end of the formatting code.
# \033[0m resets the formatting, ensuring that any text printed after it is not bold.
for name in names: # loop for printing names
    print(name) # prints name

# Print birthdates section
print("\033[1m \nBirthdate \033[0m") # prints birthdate in the next line (also in bold)
for birthdate in birthdates: # loop for printing birthdates
    print(birthdate) # prints birthdate


