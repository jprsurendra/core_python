# Understanding about classes and objects/instances

In object-oriented terminology, a class is a template for defining objects. It may contains some variables that can exist in an object, as well as "methods"--procedures for operating on those variables. 

A class can be thought of as a `"type"`, with the objects(or instances) being a `"variable"` of that type. 

Multiple objects/instances of a class can be created in a single program, just like you declare multiple variables of the same type (int, string etc...) in any program.


# Magic Methods and Operator Overloading

The so-called magic methods are special methods with fixed names. They are the methods with this clumsy syntax, i.e. the double underscores at the beginning and the end. 
How do you pronounce or say a method name like `__init__`? "Underscore underscore init underscore underscore" sounds horrible and is almost a tongue twister. "Double underscore init double underscore" is a lot better, but the ideal way is "dunder init dunder" That's why magic methods methods are sometimes called dunder methods!

## What’s the difference between `__str__` and `__repr__`?
If both the functions return strings, which is supposed to be the object representation, what’s the difference?

Well, the `__str__` function is supposed to return a human-readable format, which is good for logging or to display some information about the object. Whereas, the `__repr__` function is supposed to return an “official” string representation of the object, which can be used to construct the object again. Let’s look at some examples below to understand this difference in a better way.
```python
    >>> import datetime
    >>> now = datetime.datetime.now()
    >>> now.__str__()
    '2020-12-27 22:28:00.324317'
    >>> now.__repr__()
    'datetime.datetime(2020, 12, 27, 22, 28, 0, 324317)'
```

## What’s the difference between `__new__` and `__init__`?

Use `__new__` when you need to control the creation of a new instance. Use `__init__` when you need to control initialization of a new instance.

[Example of simple class](https://github.com/jprsurendra/core_python/blob/main/oops/new_and_init_in_class.py) 

[Example of singleton class](https://github.com/jprsurendra/core_python/blob/main/oops/singleton.py) 

[Example of LimitedInstances](https://github.com/jprsurendra/core_python/blob/main/oops/limited_instances.py) 
 

## What does built-in class attribute `__dict__` do in Python?

`__dict__` gives a dictionary view of the object. I.e. it is an object of 'dict' type that contains the object's attributes.

You could do something fancier in Class's `__str__()` (or the `__unicode__()`) method:
```python
    def __str__(self):
        retstr = ''
        for k,v in self.__dict__.iteritems():
            retstr += '%s: %s\n' % (k, v)
        return retstr
```

## Some other special methods `__getattr__`, `__getattribute__`, `__setattr__` and `__delattr__`

These methods over-ride the default attribute/method handling … so your classes can behave as if instances dynamically have or lack attributes in just about any way you like. 

The setattr used to sets the named attribute on the given object with a specified value.

```python
    class Employee:
        pass 
     
    emp1 = Employee()
    setattr(emp1, 'Salary', 12000)
     
    emp2 = Employee()
    setattr(emp2, 'Age', 25)
     
    print(emp1.Salary)
    print(emp2.Age)

    del emp1.salary     # Delete object property
    del emp1            # Delete object
```
Sample output of above program.
```
    12000
    25
```
## Example of `__getitem__` and `__setitem__` in Python
```python
    class Counter(object):
        def __init__(self, floors):
            self._floors = [None]*floors
     
        def __setitem__(self, floor_number, data):
            self._floors[floor_number] = data
     
        def __getitem__(self, floor_number):
            return self._floors[floor_number]
     
     
    index = Counter(4)
    index[0] = 'ABCD'
    index[1] = 'EFGH'
    index[2] = 'IJKL'
    index[3] = 'MNOP'
     
    print(index[2])
```

## Aggregation and Composition in Python

Aggregation is a week form of composition. If you delete the container object contents objects can live without container object.

In composition one of the classes is composed of one or more instance of other classes. In other words one class is container and other class is content and if you delete the container object then all of its contents objects are also deleted.

[Example of Aggregation and Composition](https://github.com/jprsurendra/core_python/blob/main/oops/aggregation_and_composition.py) 

 
## Iteration Overloading Methods in Python

The `__iter__` returns the iterator object and is implicitly called at the start of loops.

The `__next__` method returns the next value and is implicitly called at each loop increment.

`__next__` raises a StopIteration exception when there are no more value to return,
which is implicitly captured by looping constructs to stop iterating.

[How to reverse a string using Iterator in Python?](https://github.com/jprsurendra/core_python/blob/main/oops/iteration.py) 


## There are four Pillars of Object Oriented Programming:
    * Abstraction 
    * Encapsulation
    * Inheritance
    * Polymorphism 
Lets try to understand...


## Encapsulation in Python

The wrapping up of data and functions into a single unit (called class) is known as encapsulation. Data encapsulation is the most striking feature of a class. The data is not accessible to the outside world, and only those functions, which are wrapped in the class, can access it. These functions provide the interface between the object’s data and the program. This insulation of the data from direct access by the program is called data hiding or information hiding.
```python
    class Encapsulation:
        __name = None
     
        def __init__(self, name):
            self.__name = name
     
        def get_name(self):
            return self.__name
 
 
    pobj = Encapsulation('Rocky')
    print(pobj.get_name())
    # print(pobj.__name) # Error: AttributeError: 'Encapsulation' object has no attribute '__name'
```

## What is the difference between abstraction and encapsulation in Python?
Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation.

where as

data encapsulation is one of the fundamentals of OOP (object-oriented programming). It refers to the bundling of data with the methods that operate on that data. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them.

Abstraction is implemented using interface and abstract class while Encapsulation is implemented using private and protected access modifier.

## Polymorphism in Python

Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

[Example of Polymorphism](https://github.com/jprsurendra/core_python/blob/main/oops/polymorphism.py) 


## Contribute

Please feel free to create pull requests and issues!