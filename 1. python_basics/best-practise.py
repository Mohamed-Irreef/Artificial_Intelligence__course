
# 1. list creation in single line
list1 = [x for x in range(10)]
print(list1)

list2 = [x for x in range(20) if x%2==0]
print(list2)

# 2. lambda arguents : expression
 
def add(a,b):
    return a+b

print(add(2,3))

# lambda function

add_result = lambda a,b : a+b
print(add_result(5,7))

# 3. Map
list3 = [1,2,3,4,5,6,7]
result_map = map(lambda x:x*2,list3)
print(list(result_map))

# 4. Filter
list4=[1,2,3,4,5,6,7,8]
even_filtered_list = filter(lambda x:x%2==0, list4)

# 5. Reduce
from functools import reduce
list4=[1,2,3]
sum_result = reduce(lambda res,x: res+x,list4)
print(sum_result)