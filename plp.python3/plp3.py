def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"Final price: ${final_price:.2f}")
