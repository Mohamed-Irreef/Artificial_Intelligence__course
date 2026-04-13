set_value={1,2,3,4,5}
print(set_value)


set_value.add(6)
print(set_value)

set_value.remove(6)
print(set_value)


set1={1,2,3}
set2={3,4,5}

print("Set properties")
# Union
print(set1 |  set2)
# Intersection
print(set1&set2)
# differences
print(set1-set2)