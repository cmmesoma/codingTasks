# python programming exercise
# while loop statement
# if statement
# casting
# arithematics

num = 0 # initial number
sum = 0 # initial sum
count = 0 #initial count
while num != -1: # makes sure the loop continues as long as the number entered is not -1
  num = float(input("Write a number or write -1 to exit: ")) # user enters number (should be float datatype to accomodate both whole numbers or decimal numbers)
  number = [] # continually asks the user to enter a number
  sum = (float(sum) + float(num)) # sum of the initial sum and the next number entered (0 + 1st float + 2nd float + etc)
  count = int(count + 1) # this should be in integer datatype because they are whole numbers

if num == -1: # this conditional statement brings the user's data entry to a halt, although -1 is being added to both sum and count variables. 
    sum = sum + 1 # this +1 eliminates -1 from the sum variable
    count = count - 1 # this also eliminates -1 from the count variable
ans = round((sum/count),2) # calculates the average (sum divided by count) and rounds it up into two decimal places 
print(str(ans)) # prints out the answer in a string data type