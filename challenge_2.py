#python programming exercise
#casting

string_fav = input("Enter your favourite restaurant: ")
int_fav = int(input( "Enter your favourite phone number: "))
print(string_fav)
print(int_fav)

int_rest = int(string_fav) # shows a Value Error: invalid literal for int() with base 10. This shows that the int function only recognises integers. When whole numbers are mixed together with strings, or floats, it will fail to calculate or execute the whole numbers as int datatype.
