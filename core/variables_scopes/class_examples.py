class Car:
    wheels = 4  # Class variable shared by all instances
    # Static (or class) variable
    manufacturer = "Generic Motors"

    def __init__(self, color):
        self.color = color  # Instance variable

    @staticmethod
    def car_info():
        return "Cars have wheels and an engine."

    '''
        1. Note that str() and repr() return the same value, because str() calls __repr__() when __str__() isn’t implemented.
    '''
    def __repr__(self):
        both_are_equals = False
        if self.wheels == Car.wheels:
            both_are_equals = True
        return f"Car[color: {self.color}, wheels: {self.wheels}, Car.wheels: {Car.wheels}, Both 'wheels' are equals: {both_are_equals}] "


if __name__ == "__main__":
    # All Car instances share the class variable 'wheels'
    car1 = Car("Red")
    car2 = Car("Blue")

    print("car1: ", car1)
    print("car2: ", car2)

    # Changing the class variable affects all instances
    Car.wheels = 5

    print("car1: ", car1)
    print("car2: ", car2)

    # Static methods can be called on the class without an instance
    print(Car.car_info())  # Output: Cars have wheels and an engine.

    # Accessing static variables using class and instances
    print(Car.manufacturer)  # Access via class: Output - Generic Motors

    print(car1.manufacturer)  # Access via instance: Output - Generic Motors
    print(car2.manufacturer)  # Access via instance: Output - Generic Motors

    # Modifying the static variable via class affects all instances
    Car.manufacturer = "Advanced Motors"
    print(car1.manufacturer)  # Output - Advanced Motors
    print(car2.manufacturer)  # Output - Advanced Motors



