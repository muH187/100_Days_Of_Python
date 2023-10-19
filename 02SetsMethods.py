s1 = {1, 4, 5, 6, 8}
s2 = {2, 3, 4, 7, 8}

print(s1)
s1.update(s2)
print(s1)
#
# cities = {"Karachi", "Delhi", "Mumbai", "Lahore", "Islamabad", "Tokyo", "Texas"}
# cities2 = {"Delhi", "Madrid", "Kabul", "Moscow", "Berlin", "Lahore", "Paris"}
# # cities.update(cities2)
# # print(cities)
#
# # cities3 = cities.difference(cities2)
# # print(cities3)
#
# cities3 = cities.intersection(cities2)
# print(cities3)

cities = {"Karachi", "Lahore", "Islamabad", "Multan"}
# cities.add("Quetta")
# print(cities)

# cities.remove("Lahore")
# print(cities)

# cities.discard("Malir")
# print(cities)

item = cities.pop()
print(cities)
print(item)