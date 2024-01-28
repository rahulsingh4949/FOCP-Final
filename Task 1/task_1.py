def calculate_price(num_pizzas, delivery, is_tuesday, used_app):
    # Constants for pizza price, delivery cost, and app discount
    pizza_price = 12.00
    delivery_cost = 2.50
    app_discount = 0.25

    # Apply Tuesday discount
    if is_tuesday:
        # Half price on Tuesdays
        pizza_price = 6.00

    # Calculate total pizza cost
    total_pizza_cost = num_pizzas * pizza_price

    # Add delivery cost if required and number of pizzas is less than 5
    if delivery and num_pizzas < 5:
        total_pizza_cost += delivery_cost

    # Apply app discount if the app is used
    if used_app:
        total_pizza_cost *= (1 - app_discount)

    # Return the total cost rounded to 2 decimal places
    return round(total_pizza_cost, 2)


def main():
    # Introduction
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Input validation for the number of pizzas
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    # Input validation for delivery option
    while True:
        delivery_input = input("Is delivery required? (Y/N) ").lower()
        if delivery_input in ('y', 'n'):
            delivery = delivery_input == 'y'
            break
        else:
            print('Please answer "Y" or "N".')

    # Input validation for Tuesday
    while True:
        tuesday_input = input("Is it Tuesday? (Y/N) ").lower()
        if tuesday_input in ('y', 'n'):
            is_tuesday = tuesday_input == 'y'
            break
        else:
            print('Please answer "Y" or "N".')

    # Input validation for app usage
    while True:
        app_input = input("Did the customer use the app? (Y/N) ").lower()
        if app_input in ('y', 'n'):
            used_app = app_input == 'y'
            break
        else:
            print('Please answer "Y" or "N".')

    # Calculate and display the total price
    total_price = calculate_price(num_pizzas, delivery, is_tuesday, used_app)
    print(f"\nTotal Price: £{total_price:.2f}.")

# Run the main function
main()