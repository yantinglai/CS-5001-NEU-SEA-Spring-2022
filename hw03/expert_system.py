""" This is a Fever diagnosis system."""
# What else to improve for this code? The exception handle for input other than (Yes, No, Y, N)
def cough():
    """
    This is a cough function.
    """
    ans = input("Are you coughing? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        wheez_phlegm()
    elif ans in ('n',"no"):
        headache()

def headache():
    """
    This is a headache function.
    """
    ans = input("Do you have a headache? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        various_pain()
    elif ans in ('n',"no"):
        aching_bones_joints()

def various_pain():
    """
    This is a various pain function.
    """
    ans = input("Are you experiencing any of the following pain when bending your head forward "+
    "nausea or vomitting, bright light hurting your eyes, drowsiness or confusion? "+
    "Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include menigtis.")
    elif ans in ('n',"no"):
        vomit_diarrhea()

def vomit_diarrhea():
    """
    This is a diarrhea function.
    """
    ans = input("Are you vomitting or had diarrhea? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include digestive tract infection.")
    elif ans in ('n',"no"):
        aching_bones_joints()

def wheez_phlegm():
    """
    This is a wheez function
    """
    ans = input("Are you short of breath or wheezing or coughing up phlegm? \
Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include pneumonia or infection of airways")
    elif ans in ('n',"no"):
        headache_after_cough()

def headache_after_cough():
    """
    This headache after cough function.
    """
    ans = input("Do you have a headache? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include viral infection")
    elif ans in ('n',"no"):
        aching_bones_joints()

def aching_bones_joints():
    """
    This is an aching bones and joints function.
    """
    ans = input("Do you have aching bones or joints? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include viral infection")
    elif ans in ('n',"no"):
        rash()

def rash():
    """
    This is a rash function.
    """
    ans = input("Do you have a rash? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Insufficient information to list possibilities.")
    elif ans in ('n',"no"):
        sore_throat()

def sore_throat():
    """
    This is a sore throat function.
    """
    ans = input("Do you have a sore throat? Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include a throat infection.")
    elif ans in ('n',"no"):
        back_pain()

def back_pain():
    """
    This is a back pain function.
    """
    ans = input("Do you have back pain just above the waist with chills and fever? \
Please enter Y or N \n").lower()
    if ans in ('y',"yes"):
        print("Possibilities include kidney infection.")
    elif ans in ('n',"no"):
        urinate_pain()

def urinate_pain():
    """
    This is a urinate pain function.
    """
    ans = input("Do you have pain urinating or are urinating more often? Please enter Y or N \n")
    ans = ans.lower()
    if ans in ('y',"yes"):
        print("Possibilities include a urinary tract infection.")
    elif ans in ('n',"no"):
        sun_hot_conditions()

def sun_hot_conditions():
    """
    This is a hot condition function.
    """
    ans = input("Have you spent the day in the sun or in hot conditions? Please enter Y or N \n")
    ans = ans.lower()
    if ans in ('y',"yes"):
        print("Possibilities sunstroke or heat exhaustion.")
    elif ans in ('n',"no"):
        print("Insufficient information to list possibilities.")
    else:
        print("Please give a valid input: ")
        sun_hot_conditions()

cough()
