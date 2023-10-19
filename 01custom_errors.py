# a = int(input("Enter a number between 3 and 10: "))
# if a<3 or a>10:
#     raise ValueError("The must be in between 3 and 10")
# print(a)

b = input("Please Enter an integer number: ")
if b == "quit":
    print()
else:
    if int(b)<3 or int(b)>10:
        raise ValueError("The integer should be in between 3 and 10.")
print(b)