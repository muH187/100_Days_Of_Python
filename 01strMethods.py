# strings are immutable
a = "!!Harry!!!!!!!!!Harry"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))

b = "i love pYthon"
print(b.capitalize())

str1 = "Welcome to The Console"
print(str1)
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("Console"))
print(str1.endswith("l"))

str2 = "He's  name is Dan. He is an honest man"
print(str2.find("is"))
print(str2.find("ishh"))
# print(str2.index("isss")) throws an error

str3 = "WelcomeToTheConsole"
print(str3.isalnum())

str3 = "Welcome1"
print(str3.isalpha())

str3 = "welcome to the world"
print(str3.islower())

str3 = "Merry Christmas\nTo My Friends"
print(str3)
print(str3.isprintable())

str3 = "  "
print(str3.isspace())

str3 = "World Health Organization"
print(str3.istitle())

str3 = "To kill a mocking Bird"
print(str3.istitle())

str3 = "Python is a programming language"
print(str3.startswith("Python"))

str3 = "i lOVE pYTHON"
print(str3.swapcase())

str3 = "His name is Dan. Dan is an honest man"
print(str3.title())