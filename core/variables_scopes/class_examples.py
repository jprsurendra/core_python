class MyClass:
    # Static (class) variable
    static_variable = 0

    def __init__(self, value):
        self.instance_variable = value
        self.static_variable=0
        print('self.instance_variable: ', self.static_variable)
        MyClass.static_variable += 1
        print('self.instance_variable: ', self.static_variable)



# Test the static variable
if __name__ == "__main__":
    # obj1 = MyClass(1)
    # obj2 = MyClass(2)
    # obj3 = MyClass(3)
    #
    # print(f"obj1.instance_variable = {obj1.instance_variable}")  # Output: 1
    # print(f"obj2.instance_variable = {obj2.instance_variable}")  # Output: 2
    # print(f"obj3.instance_variable = {obj3.instance_variable}")  # Output: 3
    #
    # print(f"MyClass.static_variable = {MyClass.static_variable}")  # Output: 3
    # print(f"obj1.static_variable = {obj1.static_variable}")  # Output: 3
    # print(f"obj2.static_variable = {obj2.static_variable}")  # Output: 3
    # print(f"obj3.static_variable = {obj3.static_variable}")  # Output: 3
    final_results_list = [1,2,3,4,5,6]
    x = int(round(len(final_results_list) / 2, 0))
    print(x)
