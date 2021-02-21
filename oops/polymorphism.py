# Creating a shape Class
class Shape:
    width = 0
    height = 0

    # Creating area method
    def area(self):
        print("Parent class Area ... ")


# Creating a Rectangle Class
class Rectangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Overridding area method
    def area(self):
        print("Area of the Rectangle is : ", self.width * self.height)


# Creating a Triangle Class
class Triangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Overridding area method
    def area(self):
        print("Area of the Triangle is : ", (self.width * self.height) / 2)


rectangle = Rectangle(10, 20)
triangle = Triangle(2, 10)

rectangle.area()
triangle.area()