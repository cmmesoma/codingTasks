# Python programming task
# a program that allows a user to register students for an exam venue.
# open(), write(), input() and range () functions are used.
# for loop statement is used

# Ask user for the number of students
num_students = int(input("Please enter the number of students registering: ")) # user enters the total number of students

# Open reg_form.txt in write mode
with open("reg_form.txt", "w") as file:
    file.write("\nAttendance Register\n ") # prints Attendance Register as a title in the reg_form.txt

    # Write student IDs to the file with dotted lines
    for i in range(num_students): # loop for producing the attendance register is created. the loop is only run subject to the total student number. the total number of students becomes the total number of entries.
        # for instance, if the num_students is 10, it will only allow the user to enter only 10 student ID before it closes the program.
        student_id = input("Enter student ID number: ") # user enters student id
        
        file.write(student_id + " ...............\n") # Includes a dotted line after each student ID

print("The Attendance Register created successfully!") # prints The Attendance Register created successfully! after the number of entries is exhausted.

