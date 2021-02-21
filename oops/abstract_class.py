'''
    What is an abstract class in Python?

    1. Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared,
but contains no implementation. Abstract classes may not be instantiated, and require sub-classes to provide implementations
for the abstract methods

    2. Making the __init__ an abstract method

'''

from abc import ABC, ABCMeta, abstractmethod


class AbstractClass1(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def eat(self):
        pass


class AbstractClass2(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, n):
        self.n = n


class AbstractClass3(ABC):
    def __init__(self, username):
        self.username = username
        super().__init__()

    @abstractmethod
    def name(self):
        pass

class Parents(AbstractClass1):
    def eat(self):
        return "Eat solid food " + str(self.value) + " times each day."


class Babies(AbstractClass1):
    def eat(self):
        return "Milk only " + str(self.value) + " times or more each day."



class Employee(AbstractClass2):
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

'''
Make an abstract class inherit from another abstract class
A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.
'''
class B(AbstractClass3):
    @abstractmethod
    def age(self):
        pass

class C(B):
    def name(self):
        print(self.username)

    def age(self):
        return

def main():
    food = 3
    adult = Parents(food)
    print('Adult')
    print(adult.eat())

    infant = Babies(food)
    print('Infants')
    print(infant.eat())

    print("===================")

    emp1 = Employee(10000, "John Doe")
    print(emp1.salary)
    print(emp1.name)

    print("===================")

    c = C('Test1234')
    c.name()

if __name__ == "__main__":
    main()