'''
Python has no way to enforce a variable to be a constant.
The nearest you can go is to use an enum:

And get to each value using for example:
Constants.WIDTH.value

'''
from enum import Enum

class Constants(Enum):
	WIDTH = 1024
	HEIGHT = 256

print(Constants.WIDTH.value)
#Output: State.ACTIVE