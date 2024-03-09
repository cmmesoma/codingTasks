#python programming task
#this helps to improve our practical knowledge of int and str functions.
#casting, arithematics

print("Hello user, in this exercise you will give me 3 different integers of your choice. Let's go!") # A welcome remark prempting the user on what to do.
int_1 = int(input("Enter your first integer: ")) # user enters first integer
int_2 = int(input("Enter your second integer: ")) # user enters second integer
int_3 = int(input("Enter your third integer: ")) # user enters last allowed integer
sum = str(int_1 + int_2 + int_3) #the total sum of the 3 integers converted from an integer datatype to a string datatype (casting)
print("The sum of all the numbers is " + sum) # prints out the sum
sub1_2 = str(int_1 - int_2) # the difference between the first integer and the second integer (converted in a string datatype)
print("The first number minus the second number is " + sub1_2) # prints out the difference
multi3_1 = str(int_3 * int_1) # the multiplication of integer 3 by integer 1 (converted in a string datatype)
print("The third number multiplied by the first number is " + multi3_1) # prints out the product
num_ave = str((int_1 + int_2 + int_3)/int_3) # the sum of all the integers divided by the third integer
print("The sum of all three numbers divided by the third number is " + num_ave) # prints out the solution

