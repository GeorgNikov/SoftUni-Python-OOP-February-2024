from project import Table


class InsideTable(Table):
    MIN_TABLE_NUMBER = 1
    MAX_TABLE_NUMBER = 50
    ERROR_MESSAGE = "Inside table's number must be between 1 and 50 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)
