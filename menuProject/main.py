def main():
    meals = {
        1: ("Classic Burger", 5.99),
        2: ("Cheese Burger", 6.99),
        3: ("Bacon Burger", 7.99),
        4: ("Veggie Burger", 5.99),
        5: ("Chicken Burger", 6.49),
        6: ("Fish Burger", 6.99),
    }

    price_fries = 1.99
    price_drink = 1.49

    print("Welcome to CodeBurger! Order and enjoy!")

    for key, (name, price) in meals.items():
        print(f"{key}: {name} - ${price:.2f}")

    total_cost = 0.0

    num_meals = int(input("How many meals would you like to order? "))

    for i in range(num_meals):
        choice = int(input("Please choose your meal by number: "))
        while choice not in meals:
            print("Invalid choice, please select a valid number from the menu.")
            choice = int(input("Please choose your meal by number: "))

        meal_price = meals[choice][1]
        total_cost += meal_price

        fries = input(f"Would you like to add fries for an additional ${price_fries:.2f}? (yes/no) ")
        if fries.lower() == 'yes':
            total_cost += price_fries

        drink = input(f"Would you like to add a drink for an additional ${price_drink:.2f}? (yes/no) ")
        if drink.lower() == 'yes':
            total_cost += price_drink

        print(f"Subtotal for this meal: ${total_cost:.2f}\n")
    
    print(f"Your total order cost is: ${total_cost:.2f}")

main()
