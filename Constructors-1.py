class Person():
    def __init__(self, n, o):
        
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Ali", "Businessman")
b = Person("Aisha", "Software Engineer")
a.info()
b.info()
# a.name = "Ali"
# a.occupation = "Businessman"
# a.info()