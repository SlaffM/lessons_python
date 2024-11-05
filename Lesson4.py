l1 = ['a','aaaaaaaaa','nhnh']
l2 = [1,1,1]
l3 = [2,2,2]

lgen = [l1,l2,l3]
# print(lgen)
# for el in lgen:
#     for el_in in el:
#         print(el_in)

d1 = {1: 111, 2: 222, 3: 333}
# for el in d1.keys():
#     print(el, d1.get(el))

# v1 = 1
# while True:
#     print(v1)
#     v1 += 1
#     if v1 > 10:
#         break

d2 = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}
d3 = dict()

d3 = d1.copy()
for el in d2.keys():
    d3[el] = d2.get(el)

print(d3)


