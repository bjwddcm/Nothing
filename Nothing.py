# 创建字典方法
a = {"name": 12}
b = [['name', 12]]

c = list(range(1, 10))
d = dict.fromkeys(c, 12)
# print(d)

keys = [1, 2, 3]
values = [1, 2, 3]
e = dict(zip(keys, values))
print(e)
# **************************************

print(e.keys())
print(e.values())
print(e.items())
