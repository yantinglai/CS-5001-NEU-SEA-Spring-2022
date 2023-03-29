"""A Class representing a company."""
from offer import Offer


class Company:
    """A class representing a company"""

    def __init__(self, name):
        """
        Initialzing a company's name and list of employees
        """
        self.name = name
        self.list_of_employees = []

    def make_offer(self, person, salary):
        """
        Company makes offer to candidate
        """
        offer = Offer(self, person, salary)
        print(f"{self.name}'s offer: {person.name}, {offer.salary}")
        return offer

    def print_company_profile(self):
        """
        Print out company profile
        """
        if len(self.list_of_employees) == 0:
            print(f"{self.name}:")
        for employee in self.list_of_employees:
            print(f"{self.name}: {employee.name}")

    def terminate(self, person):
        """
        Company terminates a person's employment
        """
        terminated_person_list = list(filter(
            lambda x: x.name != person.name, self.list_of_employees))
        if terminated_person_list:
            terminated_person = terminated_person_list[0]
            terminated_person.salary = None
        print(f"{self.name} has terminated the contract with {person.name}")
        print(f"{self.name}'s current list of employees:", end=" ")
        print(len(terminated_person_list))


#  terminated_person_list = list(filter(
#             lambda x: x.name != person.name, self.list_of_employees))
#  我写成了：x == person.name 也达到了同样的效果，但是这之间究竟发生了什么
#  如果写的是 x != person.name，程序并没有把这个person的name去掉，why？
#  x 是什么， x 是一个 object，所以不存在 x==person.name，
#  这个时候，python就会把list里面所有和这个条件相反的元素全部清除掉，所以是凑巧写对
