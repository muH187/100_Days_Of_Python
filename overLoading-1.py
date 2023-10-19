class Area:
    def find_area(self, x=None, y=None):

        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

area = Area()
area.find_area()
area.find_area(5)
area.find_area(5,10)