class A:
    def __init__(self, x):
        print(" -----  inside __init__()  -----")
        self.y = x

    def __call__(self):
        res = 0
        print(" -----  inside __call__()  ----- adding 2 to the value of y")
        res = self.y + 2
        return res

    def __str__(self):
        print(" -----  inside __str__()  ----- value of y: ", str(self.y))
        return str(self.y)

    # declaration of instance of class A

def main():
    # declaration of instance of class A
    a = A(3)

    # calling __str__() for a
    a.__str__()
    print(" -----  ----------------  -----")
    # calling __call__() for a
    r = a()
    print(r)
    print(" -----  ----------------  -----")
    # declaration of another instance of class A
    b = A(10)

    # calling __str__() for b
    b.__str__()
    print(" -----  ----------------  -----")
    # calling __call__() for b
    r = b()
    print(r)
    print(" -----  ----------------  -----")

if __name__ == "__main__":
    main()