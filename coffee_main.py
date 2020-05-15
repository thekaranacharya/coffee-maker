# Write your code here
class CoffeeMachine :
    # class attributes
    machine_state = 'main_action_state'
    fill_index = -1
    units_list = ['ml of water', 'ml of milk', 'grams of coffee beans', 'disposable cups of coffee']

    water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available = 400, 540, 120, 9, 550

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

    def work_with_input(self, command):
        if self.machine_state == 'main_action_state':
            if command == 'buy':
                self.buy('start')
            elif command == 'fill':
                self.fill('start')
            elif command == 'take':
                self.take()
            elif command == 'remaining':
                self.show_available_supplies()
        elif self.machine_state == 'buy_state':
            self.buy(command)
        elif self.machine_state == 'fill_state':
            self.fill(command)

    def show_available_supplies(self):
        self.machine_state = 'main_action_state'  # changing back to the original state
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

    def is_coffee_available(self, coffee_index):
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

        if min_cups_possible > 0:
            return True
        else:
            # if min_cups_possible = 0 i.e. either of the ingredients is 0
            ingredients = [cups_with_water, cups_with_milk, cups_with_beans]
            return ingredients.index(min(ingredients))

    def buy(self, command):
        if command == 'start':
            self.machine_state = 'buy_state'
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        elif command == 'back':
            self.machine_state = 'main_action_state'
            return
        else:
            self.machine_state = 'main_action_state'
            coffee_index = command
            if self.disposable_cups_available > 0:
                prep_status = self.is_coffee_available(int(coffee_index))
                if prep_status:  # if True
                    print('I have enough resources, making you a coffee!')
                    self.disposable_cups_available -= 1

                    if coffee_index == '1':
                        # espresso
                        # subtracting the quantity of ingredients
                        self.water_available -= self.espresso_water
                        self.milk_available -= self.espresso_milk
                        self.coffee_beans_available -= self.espresso_beans
                        # adding the cost to the money
                        self.money_available += self.espresso_cost

                    elif coffee_index == '2':
                        # latte
                        # subtracting the quantity of ingredients
                        self.water_available -= self.latte_water
                        self.milk_available -= self.latte_milk
                        self.coffee_beans_available -= self.latte_beans
                        # adding the cost to the money
                        self.money_available += self.latte_cost

                    elif coffee_index == '3':
                        # cappuchino
                        # subtracting the quantity of ingredients
                        self.water_available -= self.cappu_water
                        self.milk_available -= self.cappu_milk
                        self.coffee_beans_available -= self.cappu_beans
                        # adding the cost to the money
                        self.money_available += self.cappu_cost

                else:
                    ingredients_list = ['water', 'milk', 'coffee beans']
                    print('Sorry, not enough {}!'.format(ingredients_list[prep_status]))

            else:
                print('Sorry, not enough disposable cups!')

    def fill(self, command):
        if command == 'start':
            self.machine_state = 'fill_state'
        else:
            quantity_to_add = command
            if self.fill_index == 0:
                self.water_available += int(quantity_to_add)
            elif self.fill_index == 1:
                self.milk_available += int(quantity_to_add)
            elif self.fill_index == 2:
                self.coffee_beans_available += int(quantity_to_add)
            elif self.fill_index == 3:
                self.disposable_cups_available += int(quantity_to_add)

        if -1 <= self.fill_index < 3:
            self.fill_index += 1
            print(f'Write how many {self.units_list[self.fill_index]} do you want to add:')
        else:
            self.fill_index = -1
            self.machine_state = 'main_action_state'



    def take(self):
        self.machine_state = 'main_action_state'  # changing back to the original state
        print("I gave you ${}".format(self.money_available))
        self.money_available = 0


#   ----------------------- main program execution starts here -------------------------

coffee_machine = CoffeeMachine()
while True:
    if coffee_machine.machine_state == 'main_action_state':
        print("Write action (buy, fill, take, remaining, exit):")
    command = input()  # input() will be taken irrespective of the machine_state
    if command == 'exit':
        break
    else:
        coffee_machine.work_with_input(command)
