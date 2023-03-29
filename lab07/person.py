"""A person Class"""
from company import Company


class Person:
    """
    A class representing a person
    """

    def __init__(self, name, age):
        """
        Initializing a person with name and age
        """
        self.name = name
        self.age = age
        self.salary = None  # initialize as None 啥意思
        self.offer = None
        self.cv = []

    def introduce_self(self):
        """
        Prints out a self introduction including name, employer, and salary
        """
        print(f"Hi I'm, {self.name}")
        if self.offer is not None:
            print(f"I work for {self.offer.fromCompany.name}", end=" ")
            print(f"and my salary is {self.offer.salary}")

    def accept(self, offer):
        """
        A person acceopts an offer
        """
        if self.offer is not None:
            print(
                f"Hi, {self.name}. I'm afraid there's been a misunderstanding.\
You can't have more than one job.")
            return
        self.offer = offer  # pass the particular offer
        offer.accepted(self)   # check if offer is valid or not

    def quit(self, company):
        """
        A person quits his or her job
        """
        company.list_of_employees = list(
            filter(lambda x: x.name != self.name, company.list_of_employees))
        self.company = None
        self.salary = None

        print(f"{self.name} decides to quit the job from {company.name}")
        print(f"{company.name}'s current list of employees:", end=" ")
        print(len(company.list_of_employees))

    def print_cv(self):
        """
        A list of company names that a person has worked in the past or present
        """
        for cv in self.cv:
            print(f"The company that {self.name} has worked for: {cv}")
