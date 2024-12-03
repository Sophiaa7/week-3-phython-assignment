def calculate_discount(price, discount_percent):
    
    # Calculate the final price after applying a discount.

    # Args:

    # price (float): 5000
    # discount_percent (float): 30%

    # Returns:
    #     float: The final price after applying the discount.
    
# Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        
        # Calculate the final price
        final_price = price - discount_amount
        
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price
final_price = calculate_discount(original_price, discount)
print(f"Original Price: ${original_price:.2f}")
print(f"Discount: {discount}%")
print(f"Final Price:

      
def calculate_discount(price, discount_percent):
    
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    

    # Check if the discount is 20% or higher
      
      if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        
        # Calculate the final price
        final_price = price - discount_amount
        
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price
def main():
    # Prompt the user for the original price and discount percentage
    original_price = float(input("Enter the original price: $"))
    discount = float(input("Enter the discount percentage (%): "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Print the result
    if discount >= 20:
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount: {discount}%")
        print(f"Final Price: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

if __name__ == "__main__":

