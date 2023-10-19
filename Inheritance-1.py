class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

a = Employee("Harry", 233)
a.showDetails()

a2 = Programmer("Ali", 500)
a2.showDetails()
a2.showLanguage()