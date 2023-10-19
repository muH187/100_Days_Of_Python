# f = open('mylife.textt.py', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# f = open("mylife.textt.py", 'a')
# f.write("Hello World, I am here")
# f.close()

# with open("mylife.textt.py", "a") as f:
#     f.write("My name is Muhammad Ali, I am from Karachi Pakistan")
#
# f = open("mylife.textt.py", 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in Maths is: {m1}")
#     print(f"Marks of student {i} in English is: {m2}")
#     print(f"Marks of student {i} in Computer is: {m3}")
# print(line)

f = open("myfile2.txt", 'w')
lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n"]
f.writelines(lines)
f.close()