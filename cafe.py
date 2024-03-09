# PYTHON programming task
# the aim of this task is to calculate the total stock worth in this Nigerian cafe.
# tools like lists, dicionaries, and for loop statements are used.

menu = ["Oha Soup", "Egusi Soup", "Abacha", "Moi Moi", "Rice", "Yam"] # the items sold in the cafe are added in a list.

stock = {"Oha Soup":12,
         "Egusi Soup":26,
         "Abacha":17,
         "Moi Moi":38,
         "Rice":23,
         "Yam":11
         } # a stock dictionary is created using {}. keys and values are assigned  
         # for instance, Oha Soup as key and the stock count of Oha Soup as value.



price = {"Oha Soup":100.00,
         "Egusi Soup":120.00,
         "Abacha":80.00,
         "Moi Moi":20.00,
         "Rice":50.00,
         "Yam":30.00 
         } # a price dictionary is created using {}. keys and values are assigned  
         # for instance, Oha Soup as key and the cost-price of Oha Soup as value. Since we are dealing with money, it is best to represent values in this as floats rather than integers.


# Calculate total stock
total_stock = 0 # starts from zero.
for item in menu: # loop for calculating the total stock in the cafe
    item_value = stock[item] * price[item] # item value is the product of both sums of stock value of a particular item and price value of that same item.

    total_stock += item_value # this means total_stock = total_stock + item_value, this keeps adding the next item value to total stock until all the item values are calculated

# Print the result
print("Total stock in the cafe:", total_stock)

