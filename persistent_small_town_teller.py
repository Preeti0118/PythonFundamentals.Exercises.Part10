from typing import Dict
import pickle


class Person:

    def __init__(self, person_id, first_name, last_name):
        self.id: int = person_id
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"id: {self.id}. owner: {self.first_name} {self.last_name}"


class Account:

    def __init__(self, account_number, account_type, account_owner):
        self.number: int = account_number
        self.type: str = account_type
        self.owner: Person = account_owner
        self.balance: float = 0

    def __str__(self):
        return f"number: {self.number}. type: {self.type}. balance: {self.balance}"


class Bank:

    def __init__(self):
        self.customers: Dict[int, Person] = dict()
        self.accounts: Dict[int, Account] = dict()

    def add_customer(self, customer: Person) -> None:
        if customer.id in self.customers:
            raise ValueError(f"Customer with id {customer.id} already exists.")
        else:
            self.customers[customer.id] = customer

    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError(f"{account.owner.id} is not a valid customer id.")
        elif account.number in self.accounts:
            raise ValueError(f"Account with id {account.number} already exists")
        else:
            self.accounts[account.number] = account

    def remove_account(self, account_id: int):
        if account_id in self.accounts:
            del self.accounts[account_id]
        else:
            raise ValueError(f"Account number {account_id} is invalid.")

    def deposit(self, account_id: int, amount: float):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance += round(amount, 2)
        else:
            raise ValueError(f"Account with id {account_id} does not exist.")

    def withdrawal(self, account_id, amount: float):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= round(amount, 2)

    def balance_inquiry(self, account_id: int):
        if account_id in self.accounts:
            balance = self.accounts.get(account_id).balance
            return round(balance, 2)
        else:
            raise ValueError(f"Account with id {account_id} does not exist.")

    def save_data(self):
        PersistenceUtils.write_pickle("customers.pickle", self.customers)
        PersistenceUtils.write_pickle("accounts.pickle", self.accounts)

    def load_data(self):
        self.customers = PersistenceUtils.load_pickle("customers.pickle")
        self.accounts = PersistenceUtils.load_pickle("accounts.pickle")


class PersistenceUtils:

    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as handler:
            pickle.dump(data, handler)

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, 'rb') as handler:
            data = pickle.load(handler)
        return data


