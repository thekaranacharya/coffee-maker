# Write your code here
class CoffeeMachine :
    # class attributes
    machine_state = None
    current_user_input = None  # this will constantly get updated as the program executes

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

    def __init__(self) :
        self.machine_state = 'off'

    def work_with_input(self, user_input):

        if self.machine_state == 'main_action_state' :

            if user_input == 'buy' :
                self.machine_state = 'buy_state'
                self.buy()
            elif user_input == 'fill' :
                self.machine_state = 'fill_state'
                self.fill()
            elif user_input == 'take' :
                self.machine_state = 'take_state'
                self.take()
            elif user_input == 'remaining' :
                self.machine_state = 'show_state'
                self.show_available_supplies()

        elif self.machine_state == 'buy_state' or self.machine_state == 'fill_state':
            # simply updates the user_input in this function
            # which was received from the external function get_input() to the class attribute user_input
            self.current_user_input = user_input

    def show_available_supplies(self) :
        available_supplies = """
            The coffee machine has:
            {} of water
            {} of milk
            {} of coffee beans
            {} of disposable cups
            ${} of money
            """.format(self.water_available,
                       self.milk_available,
                       self.coffee_beans_available,
                       self.disposable_cups_available,
                       self.money_available)

        print(available_supplies)
        self.machine_state = 'main_action_state'

    def is_coffee_available(self, coffee_index) :

        if coffee_index == 1 :
            water_per_cup = self.espresso_water
            milk_per_cup = self.espresso_milk
            beans_per_cup = self.espresso_beans
        elif coffee_index == 2 :
            water_per_cup = self.latte_water
            milk_per_cup = self.latte_milk
            beans_per_cup = self.latte_beans
        elif coffee_index == 3 :
            water_per_cup = self.cappu_water
            milk_per_cup = self.cappu_milk
            beans_per_cup = self.cappu_beans

        cups_with_water = self.water_available // water_per_cup
        cups_with_milk = 1000  # large number

        if milk_per_cup != 0 :
            cups_with_milk = self.milk_available // milk_per_cup

        cups_with_beans = self.coffee_beans_available // beans_per_cup
        min_cups_possible = min(cups_with_water, cups_with_milk, cups_with_beans)

        if min_cups_possible > 0 :
            return True
        else :
            # if min_cups_possible = 0 i.e. either of the ingredients is 0
            ingredients = [cups_with_water, cups_with_milk, cups_with_beans]
            return ingredients.index(min(ingredients))

    def buy(self) :
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        get_input()
        coffee_index = self.current_user_input

        if coffee_index == 'back' :
            return

        if self.disposable_cups_available > 0 :

            prep_status = self.is_coffee_available(int(coffee_index))

            if prep_status :  # if True

                print('I have enough resources, making you a coffee!')
                self.disposable_cups_available -= 1

                if coffee_index == '1' :
                    # espresso
                    # subtracting the quantity of ingredients
                    self.water_available -= self.espresso_water
                    self.milk_available -= self.espresso_milk
                    self.coffee_beans_available -= self.espresso_beans
                    # adding the cost to the money
                    self.money_available += self.espresso_cost

                elif coffee_index == '2' :
                    # latte
                    # subtracting the quantity of ingredients
                    self.water_available -= self.latte_water
                    self.milk_available -= self.latte_milk
                    self.coffee_beans_available -= self.latte_beans
                    # adding the cost to the money
                    self.money_available += self.latte_cost

                elif coffee_index == '3' :
                    # cappuchino
                    # subtracting the quantity of ingredients
                    self.water_available -= self.cappu_water
                    self.milk_available -= self.cappu_milk
                    self.coffee_beans_available -= self.cappu_beans
                    # adding the cost to the money
                    self.money_available += self.cappu_cost

            else :
                ingredients_list = ['water', 'milk', 'coffee beans']
                print('Sorry, not enough {}!'.format(ingredients_list[prep_status]))

        else :
            print('Sorry, not enough disposable cups!')

        self.machine_state = 'main_action_state'

    def fill(self) :

        print("Write how many ml of water do you want to add:")
        get_input()
        add_water = int(self.current_user_input)
        self.water_available += add_water

        print("Write how many ml of milk do you want to add:")
        get_input()
        add_milk = int(self.current_user_input)
        self.milk_available += add_milk

        print("Write how many grams of coffee beans do you want to add")
        get_input()
        add_beans = int(self.current_user_input)
        self.coffee_beans_available += add_beans

        print("Write how many disposable cups of coffee do you want to add")
        get_input()
        add_cups = int(self.current_user_input)
        self.disposable_cups_available += add_cups

        self.machine_state = 'main_action_state'

    def take(self) :
        print("I gave you ${}".format(self.money_available))
        self.money_available = 0

        self.machine_state = 'main_action_state'


#   ----------------------- main program execution starts here -------------------------

coffee_machine = CoffeeMachine()


def get_input() :
    user_input = input().strip()
    if user_input != 'exit' :
        coffee_machine.work_with_input(user_input)
    else :
        return 'exit'


while True :
    coffee_machine.machine_state = 'main_action_state'
    print("Write action (buy, fill, take, remaining, exit):")
    # only returns something if 'exit'
    if get_input() == 'exit' :
        coffee_machine.machine_state = 'off'
        break