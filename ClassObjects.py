class Person:
    name = "Ali"
    occupation = "Software Engineer"
    networth = "100 Million Dollars"
    def info(self):
        print(f"{self.name} is a {self.occupation} and his net-worth is {self.networth}")

a = Person()
b = Person()
# a.name = "Muhammad Ali"
# a.occupation = "Entreprenuer"
# print(a.name, a.occupation, a.networth)
b.name = "Aisha"
b.occupation = "Head of Sales and Marketing Department"
b.networth = "1.8 Million Dollars"

a.info()
b.info()