# python programming exercise
# for loop statement
# if and else statement
# arithematics


row = 5 # number of rows
start = 1 # first row
end = (2 * row) # this doubles the row (this is in string datatype) 
for row_num in range(start, end): # put in memory the total asterisks to produce ie. range(1,10). it shows there is going to be 9 rows in total
    asterisk_triangle = row_num if row_num <= row else end - row_num # if row_num is less than or equal to 5, produce asterisk and loop, here 1st row will have 1 asterisk, 2nd row 2 asterisks in that increasing order until it reaches the 6th row (6 = 5, this contradicts the if statement, so the else statement is initiated), the asterisk will change become 4 (declining), 7th row 3 asterisk and so on.   
    print("* " * asterisk_triangle) #prints out a beautiful asterisk triangle