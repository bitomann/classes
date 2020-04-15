from building import Building
from city import City

# Create a new city instance and add your building instances to it.
# Once all buildings are in the city, iterate the city's building
# collection and output the information about each building in the city.

eight_hundred_eighth = Building("800 8th Street", 12)
seven_hundred_seventh = Building("700 7th Street", 44)
six_hundred_sixth = Building("600 6th Street", 13)
five_hundred_fifth = Building("500 5th Street", 99)
four_hundred_forth = Building("400 4th Street", 88)

eight_hundred_eighth.purchase("Kid Frost")
seven_hundred_seventh.purchase("MC Eight")
six_hundred_sixth.purchase("Dr. Dre")
five_hundred_fifth.purchase("B. Real")
four_hundred_forth.purchase("Mr. Cartoon")

eight_hundred_eighth.construct()
seven_hundred_seventh.construct()
six_hundred_sixth.construct()
five_hundred_fifth.construct()
four_hundred_forth.construct()

megalopolis = City()

megalopolis.add_building(eight_hundred_eighth)
megalopolis.add_building(seven_hundred_seventh)
megalopolis.add_building(six_hundred_sixth)
megalopolis.add_building(five_hundred_fifth)
megalopolis.add_building(four_hundred_forth)

for building in megalopolis.buildings:
    print(f"------------------- \n{building.address.upper()}:\n  Owner: {building.owner} \
         \n  Stories: {building.stories}\n  Built: {building.date_constructed} \
         \n  Builder: {building.designer} ")