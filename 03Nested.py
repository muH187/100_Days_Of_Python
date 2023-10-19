num = int(input("Enter the value: "))

if num < 0:
    print("The value is negative!")
elif num > 0:
    if num <= 10:
        print("Your value is between 1 and 10")
    elif num > 10 and num <= 20:
        print("Your value is between 10 to 20")
    else:
        print("Your value is greater than 20")
else:
    print("Your value is Zero")
print("Python Became Happy Now")