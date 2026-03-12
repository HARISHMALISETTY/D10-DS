
# """
# copying can be done in 2 ways:
# 1.deep copy
# 2.shallow copy


# after copying, we will have original one and copied one

# if copied is updated then original may or may not updated.

# if orignal is updating when copied updated then---->?

# if original is not updating when copied updated then--->?
# """

import copy
# # x=[1,2,3]
# # y=copy.copy(x)

# # print(x)
# # print(y)

# # y[2]='hello'

# # print(x)
# # print(y)

# a=[1,2,3,[4,5,6]]
# b=copy.deepcopy(a)

# print('before updating')
# print(a)
# print(b)
# print('after updating')

# b[3][1]='hello'
# print(a)
# print(b)



orders = [
    {"order_id":101,"customer":"Ravi","product":"Laptop","price":60000,"quantity":1,"status":"Delivered"},
    {"order_id":102,"customer":"Anita","product":"Mobile","price":20000,"quantity":2,"status":"Delivered"},
    {"order_id":103,"customer":"Rahul","product":"Headphones","price":2000,"quantity":3,"status":"Cancelled"},
    {"order_id":104,"customer":"Ravi","product":"Mobile","price":20000,"quantity":1,"status":"Delivered"},
    {"order_id":105,"customer":"Divya","product":"Laptop","price":60000,"quantity":1,"status":"Delivered"},
    {"order_id":106,"customer":"Kiran","product":"Keyboard","price":1500,"quantity":2,"status":"Delivered"},
    {"order_id":107,"customer":"Rahul","product":"Mobile","price":20000,"quantity":1,"status":"Cancelled"}
]

# copied=copy.copy(orders) #if we change duplicate, it will reflects both original and duplicate.
# copied=copy.deepcopy(orders) #if we change duplicate, it will reflects only duplicate but not original.

copied[-1]['status']='Delivered'


print(copied[-1])
print(orders[-1])

