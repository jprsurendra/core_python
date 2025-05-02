'''
Enums: Enums are readable names that are bound to a constant value.
To use enums, import Enum from the enum standard library module:
    from enum import Enum

'''
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
#Output: State.ACTIVE
print(State(1))
#Output: State.ACTIVE
print(State['ACTIVE'])
#Output: State.ACTIVE

print(State.ACTIVE.value)
#Output: 1

print(list(State))
#Output: [<State.INACTIVE: 0>, <State.ACTIVE: 1>]