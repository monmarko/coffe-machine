from data import MENU
from data import resources

profit = 0


def payment(user_choice):
    coffee_cost = MENU[user_choice]["cost"]
    print(f"Please insert ${coffee_cost}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    inserted_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    change = round(inserted_money - coffee_cost, 2)
    if change < 0:
        print(f"sorry, you did't insert enough money. Here is your ${inserted_money}")
    elif change > 0:
        print(f"Enjoy your {user_choice}. Here is your ${change} change.")
        global profit
        profit += coffee_cost
        return True
        print(f"Enjoy your {user_choice}")
        return True


def resources_check(machine_resource, needed_resource, ingredient):
    if machine_resource - needed_resource >= 0:
        return True
    else:
        print(f"Sorry, there is not enough {ingredient}")
        return False


def coffee_machine():
    machine_water_resource = resources["water"]
    machine_milk_resource = resources["milk"]
    machine_coffee_resource = resources["coffee"]
    machine_profit = 0

    # print(initial_water_resource, "\n",initial_milk_resource, "\n",initial_coffee_resource)

    is_enough = True

    while is_enough:

        coffee_choice = input("What would you like? Type espresso, latte or cappuccino: ").lower()
        print(coffee_choice)

        if coffee_choice == "report":
            print(f"Water: {machine_water_resource}ml")
            print(f"Milk: {machine_milk_resource}ml")
            print(f"Coffee: {machine_coffee_resource}ml")
            print(f"Money: ${profit}")
            continue

        if coffee_choice == "off":
            is_enough = False
            continue

        water_needed = MENU[coffee_choice]["ingredients"]["water"]
        coffee_needed = MENU[coffee_choice]["ingredients"]["coffee"]
        if coffee_choice != "espresso":
            milk_needed = MENU[coffee_choice]["ingredients"]["milk"]
        else:
            milk_needed = 0

        condition_a = resources_check(machine_coffee_resource, coffee_needed, "coffee")
        condition_b = resources_check(machine_milk_resource, milk_needed, "milk")
        condition_c = resources_check(machine_water_resource, water_needed, "water")

        if condition_a and condition_b and condition_c:
            if payment(coffee_choice):
                machine_water_resource -= water_needed
                machine_milk_resource -= milk_needed
                machine_coffee_resource -= coffee_needed
                is_enough = True


coffee_machine()
