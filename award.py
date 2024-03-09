#python programming task
#this helps to improve our practical knowledge of int and str functions.
#the aim is to determine our knowledge of if, elif and else statements

swimming = int(input("Enter time used in swimming (in minutes): "))
print("Time used in swimming: " + str(swimming))

cycling = int(input("Enter time used in cycling (in minutes): "))
print("Time used in cycling: " + str(cycling))

running = int(input("Enter time used in running (in minutes): "))
print("Time used in running: " + str(running))

Total_time = (swimming + cycling + running)

print("Total time taken for triathlon: " + str(Total_time)) # prints out total time

if Total_time <= 100: # str(Total_time) will be invalid because if statements does not string values. 
    print("Provincial Colours")
elif Total_time < 106:
    print("Provincial Half Colours")
elif Total_time < 111:
    print("Provincial Scroll")
else:
    print("No Award")