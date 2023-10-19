class Employee:
  companyName = "Apple"    #class
  noOfEmployees = 0        #varibale
  def __init__(self, name):
    self.name = name             #instance
    self.raise_amount = 0.02     #variable
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()

emp3 = Employee("Ali")
emp3.companyName = "Mircrosoft"
emp3.raise_amount = 3.46
emp3.showDetails()
