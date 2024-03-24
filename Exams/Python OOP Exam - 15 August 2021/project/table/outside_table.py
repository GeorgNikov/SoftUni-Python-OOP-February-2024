from project.table.table import Table


class OutsideTable(Table):
    MIN_TABLE_NUMBER = 51
    MAX_TABLE_NUMBER = 100
    ERROR_MESSAGE = "Outside table's number must be between 51 and 100 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)
