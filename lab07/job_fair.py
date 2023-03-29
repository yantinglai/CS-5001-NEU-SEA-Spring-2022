"""CS5001: Job fair controller by YANTING LAI"""
from person import Person
from company import Company


def main():
    """
    Job fair controller
    """
    acme = Company("Acme Insurance")
    tiptop = Company("Tip Top Construction")
    ace = Company("Ace Widgets")

    marge = Person("Marge Simpson", 34)
    asterix = Person("Asterix the Gaul", 55)
    leia = Person("Leia Organa", 26)

    # Company offer to candidates
    acme_to_marge = acme.make_offer(marge, 50000)  # need to have return value
    tiptop_to_leia = tiptop.make_offer(leia, 75000)
    ace_to_marge = ace.make_offer(marge, 100000)

    # Candidates accept company's offer
    marge.accept(acme_to_marge)
    leia.accept(tiptop_to_leia)
    asterix.accept(ace_to_marge)  # Prints error message
    marge.accept(ace_to_marge)  # Prints error message

    # Company prints out employees' list
    acme.print_company_profile()
    tiptop.print_company_profile()
    ace.print_company_profile()

    # People introduce themselves
    marge.introduce_self()
    asterix.introduce_self()
    leia.introduce_self()

    # Extra Credits
    acme.terminate(marge)
    leia.quit(tiptop)
    marge.print_cv()



main()
