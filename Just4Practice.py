# num1 = 12
# num2 = 166
# num3 = 160
# print(num1 + num2 + num3)

# a = 100
# b = 150
# b = a
# print(b)

# list = ["Ali", "Pakistan", 19, 23, 55, "Bilal", 32, True, False, "Bilal", 0]
# # print(list[-8])
# # print(list.pop(5))
# # print(list.append("Yasir"))
# # print(list.append("Umer"))
# # print(list.remove(55))
# print(list)
# print(len(list))
# # print(list.count("Bilal"))

# set = {"Ali", 34, 34, 34, 64, 1, 36, 43, True, False, "Bilal", "Pakistan"}
# print(type(set))
# set2 = {"Yasir", "Zohaib", "Shahbaz", "Usman"}
# # print(set)
# # print(len(set))
# # # print(set.remove("Ali"))
# # # print(set)
# # # set.update(set2)
# # # print(set)
# # print(set.union(set2))

# dic = {"Ali": 32, "Bilal": 20, "Mirza": 35, "Zohaib": 5}
# print(dic.values())
# print(dic.keys())

# tup = ("Ali", "Bilal", "Mirza", "Umer", "Wali", "Basit", "Yasir", "Zohaib")
# # print(type(tup))
# # print(tup.count('Umer'))
# print(tup.)
# print(tup)

# print("Welcome To Coding and Decoding Center")
# start = int(input("Enter 1 for Coding and 2 for Decoding"))
# if start == 1:
#     code = input("Enter your sent.:  ")
#     if code


# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
#
# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# print("Welcome to Coding and Decoding Center")
# start = int(input("Type 1 for Code and 2 for Decode: "))
# if start == 1:
#     st = input("Enter your Message: ")
#     words = st.split(" ")
#     if len(st)>=3:
#
#         r1 = "kir"
#         r2 = "rik"
#         words = r1+st[1:] + r2+st[0]
#         print(words)
# else:
#     pass

print("Welcome to Coding and Decoding Center")
st = input("Enter your message: ")
words = st.split(" ")
coding = input("Type 1 for Coding and 2 for Decoding: ")
coding = True if coding == "1" else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if len(word)>=3:
            r1 = "kir"
            r2 = "rik"
            stnew = r1+ word[1:] + word[0] +r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew =  word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))



