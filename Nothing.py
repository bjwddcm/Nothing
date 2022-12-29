a = set(range(1, 1000))
b = set(range(2, 700))
c = []

# for i in a:
#     # print(i,end=",")
#     for j in b:
#         if i == j:
#             # print(i)
#             c.append(i)
#             # print(set(c))
#         else:
#             pass

# print(c)
# print(a - set(c))

for i in a:
    if i not in b:
        c.append(i)
        
print(set(c))