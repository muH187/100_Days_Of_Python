class MyClass():
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
    @property
    def two_value(self):
        return (2* self._value)

    @two_value.setter
    def two_value(self, new_value):
        self._value = new_value/2

obj = MyClass(10)
obj.two_value = 500
print(obj.two_value)
obj.show()