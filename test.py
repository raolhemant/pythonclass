# a = 10
# print(a)
# test = "test alfa"
# alfa = "new branch"
set = {1,"abc",3,4,5}
print(set)
#looping through items in the set
for x in set:
    print(x,end="--->")

set.add(10)
print(set)

# set.remove(14)
# print(set)

set.discard(14)
print(set)

frozon_set = frozenset({1,2,3})
print(frozon_set)

frozon_set.add(4) #error frozen_set ko add atrributes nai xaina

