print(type(100))
print(type(3.14))
print(type("Halo"))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"a": 1}))
print(type({1, 2, 3}))

x = 100
print(type(x) == int)
print(type(x) == str)

print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(x, (int, float)))

y = True
print(type(y) == int)
print(isinstance(y, int))
