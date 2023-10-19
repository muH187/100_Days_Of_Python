# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print(gmean)

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater")

def isLesser(a, b):
    pass

a = 10
b = 15
isGreater(a, b)
calculateGmean(a, b)

x = 55
y = 25
isGreater(x, y)
calculateGmean(x, y)