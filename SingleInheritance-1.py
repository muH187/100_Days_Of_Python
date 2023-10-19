class Animal:
    def run(self):
        print("This animal is running")
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Cat(Animal):
    def hunt(self):
        print("The cat is hunting")
    def run(self):
        print("The cat is running")

cat = Cat()
cat.run()
cat.sleep()