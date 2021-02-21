# Understanding classes and objects/instances

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
```
     [Example](https://github.com/jprsurendra/core_python/blob/main/oops/new_and_init_in_class.py) 
```















## Contribute

Please feel free to create pull requests and issues!