#Question 1
def calculate_discount(price, discount_percent):
   """Calculate the final price after applying a discount.

    Parameters:
    -price (float): the original price of the item.
    -discount_percent (float): the discount percentage to apply.

   returns:
    -float: the final price after applying the discount if it's 20% or higher, otherwise return the original price.
    """
   if discount_percent >=20:
       discount_amount = price * (discount_percent / 100)
       final_price = price - discount_amount 
       return final_price   
   else:
       return price 
print(calculate_discount(50000, 20))
print(calculate_discount(1000, 25))
print(calculate_discount(1000, 15))


#Question 2
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)

if discount_percent >=20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount 
    print(f"Dicount applied. The final price is: {final_price:.2f}")
else:
    print(f"No dicount applied. The original price remains: {price:.2f}")
    
