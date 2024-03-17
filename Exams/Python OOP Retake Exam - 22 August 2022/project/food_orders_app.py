from project.client import Client


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    # Helping methods
    def _get_client_by_phone_number(self, phone_number):
        client = [c for c in self.clients_list if c.phone_number == phone_number]
        return client[0] if client else None

    def _get_meal_by_name(self, meal):
        meal = [m for m in self.menu if m.name == meal]
        return meal[0] if meal else None

    def _validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def _finish_or_cancel_order(client):
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}

    def register_client(self, client_phone_number: str):
        if self._get_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # Ебаси майката

# My solution

        # if not self._get_client_by_phone_number(client_phone_number):
        #     new_client = Client(client_phone_number)
        #     self.clients_list.append(new_client)
        #
        # client = self._get_client_by_phone_number(client_phone_number)
        #
        # self._validate_menu()
        #
        # for meal_name, meal_quantity in meal_names_and_quantities.items():
        #     current_meal = self._get_meal_by_name(meal_name)
        #
        #     if meal_name not in [m.name for m in self.menu]:
        #         raise Exception(f"{meal_name} is not on the menu!")
        #
        #     if meal_quantity > current_meal.quantity:
        #         raise Exception(f"Not enough quantity of {meal_name.__class__.__name__}: {meal_name}!")
        #
        #     if meal_name not in client.ordered_meals:
        #         client.ordered_meals[meal_name] = 0
        #     client.ordered_meals[meal_name] += meal_quantity
        #
        #     client.shopping_cart.append(meal_name)
        #     current_meal.quantity -= meal_quantity
        #     client.bill += meal_quantity * current_meal.price

# Author solution

        self._validate_menu()
        if not self._get_client_by_phone_number(client_phone_number):
            self.register_client(client_phone_number)
        client = self._get_client_by_phone_number(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

# End author solution

        # return (f"Client {client_phone_number} successfully ordered "
        #         f"{', '.join(m for m in client.shopping_cart)} for "
        #         f"{client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity

        self._finish_or_cancel_order(client)
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        self._finish_or_cancel_order(client)
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
