# Python program to execute


# main directly
print("Always executed")

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    '''
       # When you try to sort the list of Student's object, At a minimum, you should specify __eq__ and __lt__ operations. 
       Then just use sorted(<<list_of_objects>>) or <<list_of_objects>>.sort()
       Otherwise Exception will occur:
         TypeError: '<' not supported between instances of 'Student' and 'Student'
    '''
    def __eq__(self, other):
        return  ( self.__class__ == other.__class__ and
                  self.__name == other.name and self.__age == other.__age )

    def __lt__(self, other):
        return self.__age < other.__age

    '''
    def __ne__(self, other):
        return self.__age != other.__age
    def __gt__(self, other):
        return self.__age > other.__age
    def __le__(self, other):
        return self.__age <= other.__age
    def __ge__(self, other):
        return self.__age >= other.__age
    '''

    def __hash__(self):
        return hash((self.__name, self.__age))


    def __str__(self):
        return "Student: {name:%s, age:%s}"%(self.__name,self.__age)

    def __repr__(self):
        return f"Student<<{self.__hash__()}>>(name:{self.__name}, age:{self.__age})"
        # return f"Student<<hash(self)>>(name:{self.__name}, age:{self.__age})"

#invoke __str__ and __repr__
# print(str(D1))
# print(repr(D1))



if __name__ == "__main__":
    print("Executed when invoked directly")
    lst= []
    lst.append(Student("Rohit", 10))
    lst.append(Student("Surendra", 11))
    lst.append(Student("Manish", 8))
    lst.append(Student("Pooja", 6))
    lst.append(Student("Bhuwan", 25))
    print(lst)

    lst2 = sorted(lst)
    print(lst2)

    lst.sort()
    print(lst)
else:
    print("Executed when imported")



'''
Output:
    Always executed
    Executed when invoked directly
    [Student<<-5241922802715972405>>(name:AAAA, age:10), Student<<-3132639429598342108>>(name:AAAA, age:11), Student<<-6856489529845274464>>(name:AAAA, age:8), Student<<-4072698873990208395>>(name:AAAA, age:6), Student<<6374970296428362712>>(name:AAAA, age:25)]
    [Student<<-4072698873990208395>>(name:AAAA, age:6), Student<<-6856489529845274464>>(name:AAAA, age:8), Student<<-5241922802715972405>>(name:AAAA, age:10), Student<<-3132639429598342108>>(name:AAAA, age:11), Student<<6374970296428362712>>(name:AAAA, age:25)]
    None
'''
