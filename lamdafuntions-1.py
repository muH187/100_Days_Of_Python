# def cal(x,y):
#     return x*y
# c = cal(10,10)
# print(c)

# def cal(a,b):
#     print(a*b)
# cal(2, 10)

# def double(b):
#     return b * 5
# funt = double(5)
# print(funt)

double = lambda x: x*10
cube = lambda x: x*x*x
avg = lambda x,y: x+y/2
def appl(fx, value):
    return 10 + fx(value)

print(double(10))
print(cube(3))
print(avg(10,40))
print(appl(lambda x: x*x+x, 2))