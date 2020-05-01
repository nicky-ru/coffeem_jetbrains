class CoffeeMachine:
    espresso = [250, 0, 16, 1, 4]  # ml of water, ml of milk, gram of coffee beans, cups, price
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]
    types_of_coffee = [espresso, latte, cappuccino]
    states = ["choosing an action", "choosing a type of coffee", "filling the coffee machine"]
    materials = ["water", "milk", "coffee beans", "cups"]

    def __init__(self, water, milk, beans, cups, money):
        self.state = self.states[0]
        self.available = [water, milk, beans, cups]
        self.money = money

    def send_input(self, user_input):
        if self.state == "choosing an action":
            if user_input == "buy":
                self.set_state(1)
                ask_coffee_type()
            elif user_input == "fill":
                self.set_state(2)
                ask_fill()
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.remaining()
            elif user_input == "exit":
                return True
        elif self.state == "choosing a type of coffee":
            self.buy_coffee(user_input)
            self.set_state(0)
        elif self.state == "filling the coffee machine":
            self.fill_machine(user_input)
            self.set_state(0)

    def set_state(self, state):
        self.state = self.states[state]

    def take_money(self):
        print("\nI gave you ${}".format(self.money))
        self.money = 0

    def remaining(self):
        print("\nThe coffee machine has:\n"
              "{} of water\n"
              "{} of milk\n"
              "{} of coffee beans\n"
              "{} of disposable cups\n"
              "${} of money".format(self.available[0],
                                    self.available[1],
                                    self.available[2],
                                    self.available[3],
                                    self.money))

    def buy_coffee(self, coffee_type):
        if coffee_type.isalpha():
            return

        coffee = self.types_of_coffee[int(coffee_type) - 1]
        lacking_ingredient = self.is_enough(coffee)
        if not lacking_ingredient:
            print("I have enough resources, making you a coffee!")
            self.available = [self.available[indx] - coffee[indx] for indx in range(4)]
            self.money += coffee[4]
        else:
            print("Sorry, not enough {}!".format(self.materials[lacking_ingredient - 1]))

    def is_enough(self, coffee):
        check = [self.available[indx] > coffee[indx] for indx in range(4)]
        return None if all(check) else check.index(False) + 1

    def fill_machine(self, materials):
        materials = materials.split()
        self.available = [self.available[indx] + int(materials[indx]) for indx in range(4)]


def ask_action():
    return my_coffee_machine.send_input(input("\nWrite action (buy, fill, take, remaining, exit):\n> "))


def ask_coffee_type():
    my_coffee_machine.send_input(input("\nWhat do you want to buy? "
                                       "1 - espresso, "
                                       "2 - latte, "
                                       "3 - cappuccino, "
                                       "back - to main menu:\n> "))


def ask_fill():
    water = input("\nWrite how many ml of water do you want to add:\n> ")
    milk = input("Write how many ml of milk do you want to add:\n> ")
    coffee_beans = input("Write how many grams of coffee beans do you want to add:\n> ")
    cups = input("Write how many disposable cups of coffee do you want to add:\n> ")
    my_coffee_machine.send_input("{} {} {} {}".format(water, milk, coffee_beans, cups))


my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    if ask_action():  # if user inputs exit, the function returns true
        break
