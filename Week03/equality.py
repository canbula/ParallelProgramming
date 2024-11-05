print("Equality")
a = 4
print(a == 4)
print(id(a) == id(4))
# print(a is 4)
print(id(a) is id(4))

print("Left-sided binding")
x, y, z = 0, 1, 2
print(x == y == z)
print(x == (y == z))
print((x == y) == z)

print("Inequality")
print(1 != 2)
print(not 1 == 2)

print("Comparison")
print(1 < 2)
print(1 <= 2)
print(1 > 2)
print(1 >= 2)

print("Chaining")
print(1 < 2 < 3)  # equivalent to 1 < 2 and 2 < 3
print(1 < 2 > 3)  # equivalent to 1 < 2 and 2 > 3
print(1 < 2 >= 3)  # equivalent to 1 < 2 and 2 >= 3
print(1 < 2 <= 3)  # equivalent to 1 < 2 and 2 <= 3
