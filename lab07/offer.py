"""A class representing a job offer"""


class Offer:
    """
    A class representing a job offer
    """

    def __init__(self, fromCompany, toCandidate, salary):
        """
        Initializing a job offer with company name, candidate name, and salary
        """
        self.fromCompany = fromCompany
        self.toCandidate = toCandidate
        self.salary = salary

    def accepted(self, person):
        """
        Update salary information when a person accepts the offer
        """
        if self.toCandidate.name == person.name:
            self.fromCompany.list_of_employees.append(person)  # add to list
            person.salary = self.salary     # update salary information
            print(
                f"{person.name} accepted the offer from \
{self.fromCompany.name} with a salary of {self.salary}")
            person.cv.append(self.fromCompany.name)

        else:
            person.offer = None
            print(
                f"Hi, {person.name}. \
I'm afraid there's been a misunderstanding. \
You can't accept this offer.")
