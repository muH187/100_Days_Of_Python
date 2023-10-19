# att = input("Enter your number: ")
# print(f"Multiplication table of {att} is: ")
#
# try:
#     for it in range(1,11):
#         print(f"{int(att)} X {it} = {int(att)*it}")
# except Exception as e:
#     print("Sorry some error has occurred")
#
# print("Some imp. line codes")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [2, 6]
    print(a[5])
except ValueError:
    print("Please enter an integer next timead:")
except IndexError:
    print("Some index error has occurred:")