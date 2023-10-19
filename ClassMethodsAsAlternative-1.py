class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromSTR(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e1 = Employee("Ali", 25000000)
print(e1.name)
print(e1.salary)

string = "Aisha-1500000"
e2 = Employee.fromSTR(string)
print(e2.name)
print(e2.salary)