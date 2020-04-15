# 1. Create an Employee type that contains information about employees of a company. 
# Each employee must have a name, job title, and employment start date.
class Employee:
    def __init__(self, name, job_title, employment_start_date):
        self.name = name
        self.job_title = job_title
        self.employment_start_date = employment_start_date

# 2. Create a Company type that employees can work for. A company should have a 
# business name, address, and industry type.
class Company:
    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)  

    def print_employees(self):
        print(f"\n{self.name} is in the {self.industry} industry and employs:")
        if self.employees:
            print("  * " + " \n  * ".join(employee.name for employee in self.employees))    

# 3. Create two companies, and 5 people who want to work for them.
west_studios = Company("West Studios", "1416 N. La Brea Ave.", "Recording")
soul_assassins_studios = Company("Soul Assassins Studios", "666 Skid Row Blvd", "Artistic Chill Zone")

b_real = Employee("B Real", "MC", "1988")
sen_dog = Employee("Sen Dog", "MC", "1989")
dj_mugs = Employee("DJ Muggs", "Beat Master", "1991")
easy_e = Employee("Easy E", "Recording Artist", "1987")
ice_cube = Employee("Ice Cube", "Actor", "1993")

# 4. Assign 2 people to be employees of the first company.
west_studios.add_employee(ice_cube)
west_studios.add_employee(easy_e)

# 5. Assign 3 people to be employees of the second company.
soul_assassins_studios.add_employee(b_real)
soul_assassins_studios.add_employee(sen_dog)
soul_assassins_studios.add_employee(dj_mugs)

# 6. Output a report to the terminal the displays a business name, and its employees.
west_studios.print_employees()
soul_assassins_studios.print_employees()