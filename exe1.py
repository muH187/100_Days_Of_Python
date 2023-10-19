a = 100
b = 15

print("The calculation of", a, "+", b, "is:", a + b)
print("The calculation of", a, "-", b, "is:", a - b)
print("The calculation of", a, "*", b, "is:", a * b)
print("The calculation of", a, "/", b, "is:", a / b)
print("The calculation fo", a, "//", b, "is:", a // b)

num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
operator = input("Enter your operation: ")

if operator == "+":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1) - int(num2))
elif operator == "*":
    print(int(num1) * int(num2))
elif operator == "/":
    print(int(num1) / int(num2))
    if num2 != 0:
        print(int(num1) / int(num2))
    else:
        print("Division is not allowed with Zero!")
else:
    print("Invalid Operation!")