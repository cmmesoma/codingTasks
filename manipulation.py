#python programming exercise
#slicing
#replace function, length function

str_manip = input("Please enter a sentence: ") # user makes an input

len_manip = len(str_manip) # len function calcualates all the number of characters including spaces

print(len(str_manip)) #prints out the total number of characters

last_manip = str_manip[len_manip-1] #prints the last character 

mod_str_manip = (str_manip.replace(last_manip, "@")) # replaces the last character of the sentence anywhere it is found in the string with @

print(mod_str_manip) # prints out the sentence with @ in it

str_mod = ((str_manip[::-1])[:3]) #reverses the entire sentence and picks out the first 3 words (in reversal)

print(str_mod) # prints out 

str_1st_3 = str_manip[:3] #removes the entire sentence except the first three character

str_last_2 = ((str_manip[::-1])[1]) + last_manip #keeps only the last two characters (in this order; the second to the last character and then the last character)

print(str_1st_3 + str_last_2) #prints out a combination of the first 3 characters and the last two characters forming a word.
