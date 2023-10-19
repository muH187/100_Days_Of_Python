num = int(input("Enter your value: "))
if num < 0:
    print(f"Your value is negative (value {num})")
elif num > 0:
    if num >= 1 and num <= 10:
        print(f"Your value is between 1 to 10 (value {num})")
    elif num >= 11 and num <= 20:
        print(f"Your value is between 11 to 20 (value {num})")
    elif num >= 21 and num <= 99:
        print(f"Your value is between 21 to 99 (value {num})")
    elif num == 100:
        print(f"Your value is 100 (value {num})")
    else:
        print(f"Your value is above 100 (value {num})")
else:
    print("Your value is Zero")