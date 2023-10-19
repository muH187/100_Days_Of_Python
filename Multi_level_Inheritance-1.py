class Organism:

    alive = True
    def sleep(self):
        print("This animal is sleeping")

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.bark()
dog.sleep()
dog.eat()