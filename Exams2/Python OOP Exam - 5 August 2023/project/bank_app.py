from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_LOAN_TYPE = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENT_TYPE = {
        "Student": Student,
        "Adult": Adult,
    }
    def __init__(self, capacity: int):
        self.capacity = capacity        # The number of clients а Bank can have.
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPE:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPE[loan_type]()
        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPE:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return f"Not enough bank capacity."

        client = self.VALID_CLIENT_TYPE[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.__find_loan_by_type(loan_type)
        client = self.__find_client_by_id(client_id)

        if loan.__class__.__name__ != client.LOAN_TYPE:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.__find_client_by_id(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans = [l for l in self.loans if l.__class__.__name__ == loan_type]
        [l.increase_interest_rate() for l in loans]

        return f"Successfully changed {len(loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients = [c for c in self.clients if c.interest < min_rate]
        [c.increase_clients_interest() for c in clients]

        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum([l.amount for c in self.clients for l in c.loans])
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0
        not_granted_sum = sum(l.amount for l in self.loans)

        result = (
            f"Active Clients: {len(self.clients)}\n"
            f"Total Income: {total_clients_income:.2f}\n"
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
            f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        )

        return result

    def __find_loan_by_type(self, loan_type):
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type]
        return loan[0] if loan else None

    def __find_client_by_id(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]
        return client[0] if client else None