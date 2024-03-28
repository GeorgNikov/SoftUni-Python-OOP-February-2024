from project import Bread
from project import Cake
from project import Tea
from project import Water
from project import InsideTable
from project import OutsideTable


class Bakery:
    FOOD_TYPE = {
        "Bread": Bread,
        "Cake": Cake,
    }

    DRINK_TYPE = {
        "Tea": Tea,
        "Water": Water,
    }

    TABLE_TYPE = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.food_names = set()
        self.drink_names = set()
        self.table_numbers = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in self.food_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.FOOD_TYPE[food_type](name, price)
        self.food_menu.append(food)
        self.food_names.add(food.name)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in self.drink_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.DRINK_TYPE[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        self.drink_names.add(drink.name)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in self.table_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.TABLE_TYPE[table_type](table_number, capacity)
        self.tables_repository.append(table)
        self.table_numbers.add(table_number)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            table = next(filter(lambda t: t.capacity >= number_of_people and not t.is_reserved, self.tables_repository))
        except StopIteration:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self._get_table_by_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        food_in_menu = [n for n in food_names if n in self.food_names]
        food_not_in_menu = [n for n in food_names if n not in self.food_names]

        foods = [self._get_food_by_name(name) for name in food_in_menu]
        [table.order_food(f) for f in foods]

        ordered_foods = '\n'.join(repr(f) for f in foods)
        missing_foods = '\n'.join(food_not_in_menu)

        return f'''Table {table_number} ordered:
{ordered_foods}
{self.name} does not have in the menu:
{missing_foods}'''

    def order_drink(self, table_number, *drink_name):
        table = self._get_table_by_number(table_number)

        if not table:
            return f'Could not find table {table_number}'

        drink_name_in_menu = [name for name in drink_name if name in self.drink_names]
        drinks_names_not_in_menu = [name for name in drink_name if name not in self.drink_names]

        drinks = [self._get_drink_by_name(drink) for drink in drink_name_in_menu]
        [table.order_drink(d) for d in drinks]

        ordered_str = '\n'.join(repr(d) for d in drinks)
        missing_str = '\n'.join(drinks_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_str}
{self.name} does not have in the menu:
{missing_str}'''

    def leave_table(self, table_number: int):
        table = self._get_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f'''Table: {table_number}
Bill: {bill:.2f}'''

    def get_free_tables_info(self):
        tables = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]

        return '\n'.join(tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def _get_table_by_number(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        return table[0] if table else None

    def _get_food_by_name(self, food_name):
        food = [f for f in self.food_menu if f.name == food_name]
        return food[0] if food else None

    def _get_drink_by_name(self, drink_name):
        drink = [d for d in self.drinks_menu if d.name == drink_name]
        return drink[0] if drink else None
