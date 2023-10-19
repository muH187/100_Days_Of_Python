x = [1, 2, 4, 5, 6]
print(dir(x))

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        self.version = 23
        self.netwroth = 100

p = Person("Ali", 19)
print(p.__dict__)