import copy

a = (1,2,3,4)
b = copy.copy(a)
c = tuple(a)

print(id(a)==id(b))
print(id(a)==id(c))
print(type(a))