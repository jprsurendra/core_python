class IntegerNumber:

    def __init__(self, num=0):
        if type(num)== int:
            self.num = num
        else:
            self.num = 0
            raise ValueError("num must be an Integer Number")

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return "IntegerNumber(" + str(self.num) + "')"

