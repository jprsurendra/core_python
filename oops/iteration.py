'''
    Iteration Overloading Methods in Python

    The __iter__ returns the iterator object and is implicitly called at the start of loops.

    The __next__ method returns the next value and is implicitly called at each loop increment.

    __next__ raises a StopIteration exception when there are no more value to return,
which is implicitly captured by looping constructs to stop iterating.

'''

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

def main_01():
    for num in Counter(5, 15):
        print(num)


class Reverse:
    def __init__(self, data):
        self.reset(data)

    def __iter__(self):
        self.index = len(self.data)
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    def reset(self, data):
        self.data = data
        # self.index = len(data)

    def do_reverse(self):
        st = ""
        for char in self:
            st = st + char
        return st


def main():
    test = Reverse('Python')
    for char in test:
        print(char)

    print(test.do_reverse())
    test.reset("Surendra")
    print(test.do_reverse())


if __name__ == "__main__":
    main_01()
    main()