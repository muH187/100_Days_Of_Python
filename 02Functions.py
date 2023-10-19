# def average(a, b):
#     print("The average is", (a+b)/2)
# average(15, 20)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))

average(19, 23,15)