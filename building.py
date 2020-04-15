import datetime

# In this exercise, you are going to define your own Building type and create
# several instances of it to design your own virtual city. Create a class
# named Building in the building.py file and define the following fields,
# properties, and methods.


class Building:
    def __init__(self, address, stories):
        self.designer = "Bito Mann"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

# Define a construct() method. The method's logic should set the date_constructed
# field's value to datetime.datetime.now(). You will need to have import datetime
# at the top of your file.
    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%-m/%-d/%Y")

# Define a purchase() method. The method should accept a single string argument of
# the name of the person purchasing a building. The method should take that string
# and assign it to the owner property.


    def purchase(self, new_owner):
        self.owner = new_owner


# Create 5 building instances
eight_hundred_eighth = Building("800 8th Street", 12)
seven_hundred_seventh = Building("700 7th Street", 44)
six_hundred_sixth = Building("600 6th Street", 13)
five_hundred_fifth = Building("500 5th Street", 99)
four_hundred_forth = Building("400 4th Street", 88)

# Have each one get purchased by a real estate magnate
eight_hundred_eighth.purchase("Kid Frost")
seven_hundred_seventh.purchase("MC Eight")
six_hundred_sixth.purchase("Dr. Dre")
five_hundred_fifth.purchase("B. Real")
four_hundred_forth.purchase("Mr. Cartoon")

# After purchased, construct each one
eight_hundred_eighth.construct()
seven_hundred_seventh.construct()
six_hundred_sixth.construct()
five_hundred_fifth.construct()
four_hundred_forth.construct()

# Once all building are purchased and constructed, print the address, owner, stories,
# and date constructed to the terminal for each one.
print(f"{eight_hundred_eighth.address} {eight_hundred_eighth.owner} \
{eight_hundred_eighth.stories} {eight_hundred_eighth.date_constructed}")