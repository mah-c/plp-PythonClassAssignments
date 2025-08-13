#function to calculte discount if discount is >= 20%
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * ((100-discount_percent)/100)
    else:
        final_price = price
    return final_price

# User input ie original price & percentage discount
price = float(input('Enter the original price: '))
discount_percent = float(input('Enter the discount percent: '))

# Output
print('Final price: ', calculate_discount(price, discount_percent))
