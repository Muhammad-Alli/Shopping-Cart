#Shopping cart with a dictionary

shopping_basket = {}
price_total = 0

while True:
    shop_item = input("Enter the item to buy or type done if you are done shopping: ")
    
    if shop_item.strip() == "": #Since this removes empty spaces at start and end, any completely empty space will be invalid too
        print("Invalid entry")
        continue 
    elif shop_item.lower() == "done":
        #print('Calculating your total, please wait...')
        break
    else:
        while True:
            #This checks if value entered is valid numeric value (greater than 0 and only numeric data type)
            try:   
                item_price = float(input(f"Enter the price of the {shop_item}: R"))
                if item_price <= 0:
                    print("Price must be greater than 0")
                    continue
                break  
            except ValueError:
                print("Invalid. Prices have to be numbers. Try again!")
        
        shopping_basket[shop_item] = item_price
        price_total += item_price    
        shop_item = ""
        item_price = 0

print("\nYour receipt:\n")
#Printed this way so the items and price show one below the other and not like {item1:price1,item2:price2, ..}
for item, price in shopping_basket.items(): #.items is a built in method attached to dictionaries returns a view of each key-value pair in dictionary into item and price seperately
    print(item + ' : R' + str(price))
print(f"\nThe total cost: R",  round(price_total, 2)) #To show 2 decimal places because when adding floating point values sometimes eventhough theres only 2 decimals it shows many
