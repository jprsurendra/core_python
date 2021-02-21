'''
Use __new__ when you need to control the creation of a new instance. Use __init__ when you need to control initialization of a new instance.
'''
class Shape:
    def __new__(cls, sides, *args, **kwargs):
        print("Creating Instance")
        if sides == 3:
            instance= Triangle(*args, **kwargs)
        else:
            instance = Square(*args, **kwargs)
        return instance  #Customize Returned Object


class Triangle:
    def __init__(self, base, height):
        print("initialization Instance of Triangle")
        self.base = base
        self.height = height

    def __str__(self):
        return "<<Triangle>> value is base: {},  height: {}".format(self.base, self.height)

    def __repr__(self):
        return f'<<Triangle>> base: {str(self.base)},  height: {str(self.height)}'


    def area(self):
        return (self.base * self.height) / 2


class Square:
    def __init__(self, length):
        print("initialization Instance of Square")
        self.length = length

    def __repr__(self):
        return "<class '__main__.Square'> length: {}".format(self.length)

    def area(self):
        return self.length * self.length

def main():
    a = Shape(sides=3, base=2, height=12)
    b = Shape(sides=4, length=2)

    print(str(a.__class__))
    print(str(a))
    print(a)
    print(a.area())

    print(str(b.__class__))
    print(b.area())

if __name__ == "__main__":
    main()