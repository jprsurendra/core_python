class MyEnum():
    __slots__ = ['TRUE', 'FALSE']

    def __init__(self, x, y):
        self.TRUE = x
        self.FALSE = y


class Person:
    __slots__ = ('name', 'age')  # Restrict to 'name' and 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.address = "123 Street" # Error: AttributeError: 'Person' object has no attribute 'address'

# Usage
p = Person("Alice", 30)
print(p.name)  # Alice
p.name = "Bob"
p.age = 35
# p.address = "123 Street"  # AttributeError: 'Person' object has no attribute 'address'


# obj = MyEnum('TRUE', 'FALSE-0')