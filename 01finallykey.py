def func1():
    try:
        p = [1,2,3,4,5,6,7]
        i = int(input("Enter your index: "))
        print(p[i])
        return 1
    except:
        print("Some error has occurred")
        return 0
    finally:
        print("I will always print")
func = func1()
print(func)