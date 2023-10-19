
# # MAP
# # def cube(x):
# #     return x*x*x
# # print(cube(4))
#
# l = [1,2,3,4,5,6,7,8,9,2]
# print(l)
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
#
#
# newl = list(map(lambda x: x*x*x, l))
# print(newl)
#
# # Filter
# def function_filter(a):
#     return a>4
# newnewl = list(filter(function_filter, l))
# print(newnewl)



# REDUCE
from functools import reduce


numbers = [1,2,3,4,5]
def mysum(x,y):
    return x + y

sum = reduce(mysum, numbers)

print(sum)