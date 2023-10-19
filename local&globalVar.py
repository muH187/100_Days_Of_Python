# x = 5
# def hello():
#     x = 10
#     print(x)
#     print("Hello Ali")
# hello()
# print(x)

x = 2

def hello():

    global x
    x = 15
    print(x)

hello()

print(x)