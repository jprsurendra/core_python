a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, same object in memory
print(a == c)  # True, same content
print(a is c)  # False, different objects in memory