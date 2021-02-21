


class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return (self.pay * 12)

'''
    Example of Aggregation in Python
    Aggregation is a week form of composition. If you delete the container object contents objects can live without container object.
'''
class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return "Total: " + str(self.pay.get_total() + self.bonus)

'''
    Example of Composition in Python
    In composition one of the classes is composed of one or more instance of other classes. In other words one class is container and other class is content and if you delete the container object then all of its contents objects are also deleted.
'''
class ComposedEmployee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


def main_aggregation():
    obj_sal = Salary(600)
    obj_emp = Employee(obj_sal, 500)
    print(obj_emp.annual_salary())

def main_composition():
    obj_emp = ComposedEmployee(600, 500)
    print(obj_emp.annual_salary())

if __name__ == "__main__":
    main_aggregation()
    main_composition()