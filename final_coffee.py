class Coffee:
    def __init__(self, water=0, milk=0, beans=0, cash=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cash = cash


class CoffeeMachine:
    input_status = "read command"
    n_fill = 0

    def __init__(self, water=400, milk=540, beans=120, cups=9, cash=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.cash = cash

    def get_command(self, command):
        if self.input_status == 'read command':
            if command == "take":
                self.take()
            elif command == "remaining":
                self.remaining()
            elif command == "fill":
                self.fill("start", 0)
            elif command == "buy":
                self.buy(0)
        elif self.input_status == 'fill_machine':
            if self.n_fill == 1:
                self.fill("water", int(command))
            elif self.n_fill == 2:
                self.fill("milk", int(command))
            elif self.n_fill == 3:
                self.fill("beans", int(command))
            elif self.n_fill == 4:
                self.fill("cups", int(command))
        elif self.input_status == 'buy_coffee':
            self.input_status = 'read command'
            if command == "back":
                return
            self.buy(int(command))

    def buy(self, val):
        if val == 0:
            self.input_status = 'buy_coffee'
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        else:
            if val == 1:
                selected_coffee = espresso
            elif val == 2:
                selected_coffee = latte
            elif val == 3:
                selected_coffee = cappuccino
            self.check_resources(selected_coffee.water, selected_coffee.milk, selected_coffee.beans, 1,
                                 selected_coffee.cash)

    def check_resources(self, w, m, b, c, csh):
        if self.water - w < 0:
            print("Sorry, not enough water!")
            return False
        if self.water - m < 0:
            print("Sorry, not enough milk!")
            return False
        if self.water - b < 0:
            print("Sorry, not enough coffee beans!")
            return False
        if self.water - c < 0:
            print("Sorry, not enough disposable cups!")
            return False
        self.water -= w
        self.milk -= m
        self.beans -= b
        self.cups -= c
        self.cash += csh
        return True

    def fill(self, stat, val):
        components = ["ml of water", "ml of milk", "grams of coffee beans", "disposable cups of coffee"]
        if stat == "start":
            self.input_status = 'fill_machine'
            self.n_fill = 1
        elif stat == "water":
            self.n_fill = 2
            self.water += val
        elif stat == "milk":
            self.n_fill = 3
            self.milk += val
        elif stat == "beans":
            self.n_fill = 4
            self.beans += val
        elif stat == "cups":
            self.n_fill = 0
            self.cups += val
            self.input_status = 'read command'

        if self.n_fill > 0 and self.input_status == 'fill_machine':
            print(f"Write how many {components[self.n_fill - 1]} do you want to add:")

    def remaining(self):
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.cash} of money")

    def take(self):
        print("I gave you $", self.cash, sep="")
        self.cash = 0


# my_machine = CoffeeMachine(400, 540, 120, 9, 550)
my_machine = CoffeeMachine()
espresso = Coffee(water=250, beans=16, cash=4)
latte = Coffee(water=350, milk=75, beans=20, cash=7)
cappuccino = Coffee(water=200, milk=100, beans=12, cash=6)
while True:
    if my_machine.input_status == "read command":
        print('Write action (buy, fill, take, remaining, exit):')
    command = input()
    if command == "exit":
        break
    else:
        my_machine.get_command(command)
    print()
