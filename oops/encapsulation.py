'''
How to create Private members of Class?
If the name of a Python function, class method, or attribute starts with (but doesn't end with) two underscores, it's private; everything else is public.
'''

class Test(object):
    __private_var = 100
    public_var = 200

    def __private_func(self):
        print('Private Function')

    def public_func(self):
        print('Public Function')
        print(self.public_var)

    def call_private(self):
        self.__private_func()
        print(self.__private_var)

def main_1():
    t = Test()
    print(t.call_private())
    print(t.public_func())

'''
Give an example of encapsulation in Python
The wrapping up of data and functions into a single unit (called class) is known as encapsulation. Data encapsulation is the most striking feature of a class. The data is not accessible to the outside world, and only those functions, which are wrapped in the class, can access it. These functions provide the interface between the object’s data and the program. This insulation of the data from direct access by the program is called data hiding or information hiding.
'''
class Encapsulation:
    __name = None

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

def main():
    pobj = Encapsulation('Rocky')
    print(pobj.get_name())
    # print(pobj.__name) # Error: AttributeError: 'Encapsulation' object has no attribute '__name'


'''
Access private members in Child class
'''


class Human():
    # Private var
    __privateVar = "this is __private variable"

    # Constructor method
    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # Public method
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # Private method
    def __privateMethod(self):
        return "Private method"

    # Public method that returns a private variable
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()

def main2():
    human = Human()
    print(human.className)
    print(human.showName("Vasya"))
    print(human.showPrivate())

    male = Male()
    print(male.className)
    print(male.showClassName())

    female = Female()
    print(female.className)
    print(female.showClassName())

if __name__ == "__main__":
    main()