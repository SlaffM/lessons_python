l1 = [1,2,3,1,1]
l2 = [11,22,33]
l3 = ["a", "b", "c"]

l_sum = set(l1 + l2 + l3)

#print(l_sum)

d1 = dict()
d1 = {1: l_sum}
#print (d1)

d1 = {1: 1, 2: 2, 3: 3}
print (d1)

d2 = {1: set(l1), 2: l2}
print(d2)

d3 = {1: d1, 2: d2}
print (d3)

print (d2.get(11))

l1 = d1.keys()
l2 = d1.values()
print(l1)
print(l2)

d1[1] = 111
print(d1)