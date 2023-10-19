

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")


# @greet
def sum(a, b):
    print(a+b)

# greet(hello)()
hello()
greet(sum)(100, 500)