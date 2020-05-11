# Write your code here
water_available = 400  # ml
milk_available = 540  # ml
coffee_beans_available = 120  # g
disposable_cups_available = 9
money_available = 550  # $

espresso_water = 250  # ml
espresso_milk = 0  # ml
espresso_beans = 16  # g
espresso_cost = 4  # $

latte_water = 350  # ml
latte_milk = 75  # ml
latte_beans = 20  # g
latte_cost = 7  # $

cappu_water = 200  # ml
cappu_milk = 100  # ml
cappu_beans = 12  # g
cappu_cost = 6  # $


def print_available_supplies():
    available_supplies = """
        The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money
        """.format(water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available)

    print(available_supplies)


def is_coffee_available(coffee_index):
    if coffee_index == 1:
        water_per_cup = espresso_water
        milk_per_cup = espresso_milk
        beans_per_cup = espresso_beans
    elif coffee_index == 2:
        water_per_cup = latte_water
        milk_per_cup = latte_milk
        beans_per_cup = latte_beans
    elif coffee_index == 3:
        water_per_cup = cappu_water
        milk_per_cup = cappu_milk
        beans_per_cup = cappu_beans
    else:
        print('Invalid index entered, please try again!')

    cups_with_milk = 1000  # large number

    cups_with_water = water_available // water_per_cup

    if milk_per_cup != 0:
        cups_with_milk = milk_available // milk_per_cup

    cups_with_beans = coffee_beans_available // beans_per_cup

    cups_possible = min(cups_with_water, cups_with_milk, cups_with_beans)
    if cups_possible > 0:
        return True
    else:
        return False


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_index = int(input().strip())

    if is_coffee_available(coffee_index):
        global water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available

        # Check if there are disposable_cups_available
        if disposable_cups_available > 0:
            # reducing the quantity of available disposable cups by 1
            disposable_cups_available -= 1

            if coffee_index == 1:
                # espresso
                # subtracting the quantity of ingredients
                water_available -= espresso_water
                milk_available -= espresso_milk
                coffee_beans_available -= espresso_beans
                # adding the cost to the money
                money_available += espresso_cost

            elif coffee_index == 2:
                # latte
                # subtracting the quantity of ingredients
                water_available -= latte_water
                milk_available -= latte_milk
                coffee_beans_available -= latte_beans
                # adding the cost to the money
                money_available += latte_cost

            elif coffee_index == 3:
                # cappuchino
                # subtracting the quantity of ingredients
                water_available -= cappu_water
                milk_available -= cappu_milk
                coffee_beans_available -= cappu_beans
                # adding the cost to the money
                money_available += cappu_cost

        else:
            print("Sorry, we don't have any disposable cups to pour coffee in. Please try again later!")

    else:
        print("Sorry, your desired coffee is not available. Please try again later!")


def fill():
    global water_available, milk_available, coffee_beans_available, disposable_cups_available

    print("Write how many ml of water do you want to add:")
    add_water = int(input().strip())
    water_available += add_water

    print("Write how many ml of milk do you want to add:")
    add_milk = int(input().strip())
    milk_available += add_milk

    print("Write how many grams of coffee beans do you want to add")
    add_beans = int(input().strip())
    coffee_beans_available += add_beans

    print("Write how many disposable cups of coffee do you want to add")
    add_cups = int(input().strip())
    disposable_cups_available += add_cups


def take():
    global money_available
    print("I gave you ${}".format(money_available))
    money_available = 0


#   ----------------------- main program execution starts here -------------------------
print_available_supplies()

print("Write action (buy, fill, take):")
action = input().strip()
if action == 'buy':
    buy()
elif action == 'fill':
    fill()
elif action == 'take':
    take()
else:
    print("Invalid action entered, please try again!")

print_available_supplies()


