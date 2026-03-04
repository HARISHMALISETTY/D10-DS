
"""
1.for loop
2.while loop

whenever we want to iterate every value/element/character in sequence types from
left to right direction. no need of using range method


for variable in seq:
    //statements

whenever we want to iterate any seq in customised way then we can use range method.


for variable in range(start,end,step):
    //statements
"""


# "data science"
# [1,2,3,4]


# str1="SOMETHING IS FISHY"
# x=1
# for char in str1:
#     print(char,str1[x])
#     x+=1




# 1st iteration-->char=S, x=1 --->S O -->x=2
# 2nd iteration-->char=O, x=2--->O M


# str1="DATA"
# for char in str1:
#     print(f"{char}-HELLO")
# """
# D-HELLO
# A-HELLO
# T-HELLO
# A-HELLO

# """

# list1=[4,6,8,2,3,1,8,9]


# for i in list1:
#     # print(i**2)
#     print(f"square of {i} is {i**2} ")

#square of 4 is 16
#square of 6 is 36


# list1=['shiva','karthik','karun','tejaswini','yamini','deepak','satwik']

# shiva length is 5
# karthik length is 7
# karun length is 5....


# for char in list1:
#     print(f"length of {char} is {len(char)}")


# nums=[3,5,7,8,2,4,6,10]
# # op=
# 0
# 5
# 14
# 24
# 8
# 20
# 36
# 70
# ind=0
# for x in nums:
#     print(f"{x*ind}")
#     ind+=1


# str1="ASDFGHJKL"
# str1="BANANA"

# {'B':1,'A':3,'N':2}




# dict1={}

# for x in str1:
#     if x in dict1:
#         dict1[x]+=1
#     else:
#         dict1[x]=1

# {'B':1,'A':3,'N':2}
# print(dict1)

# dict1['b']=0
# dict1['a']=1
# dict1['n']=2
# print(dict1)
# x=0
# for char in str1:
#     dict1[char]=x
#     x+=1
# print(dict1)



# str1='hello'
# op=str1.upper()
# print(op)

# str2='HUMAN'

# op1=str2.lower()
# print(op1)


# los=['apple','banana','SOME','hello','WELCOME','oops']

# print(los[0]==los[0].upper())
#         # 'apple'=='APPLE'
#         los[0].upper()
# op=[]
# for char in los:
#     if char==char.upper():
#         # print(char.lower())
#         op+=[char.lower()]
#     else:
#         # print(char.upper())
#         op+=[char.upper()]

# print(op)
# 'apple'--->apple==APPLE-->convert into lower
# 'banana'-->banana==BANANA-->convert into upper 
# 'SOME'--->SOME==SOME--->convert into lower 


# s1='soMetHINg'
# op=''
# # op='SOmEThinG

# for char in s1:
#     if char==char.upper():
#         op+=char.lower()
#     else:
#         op+=char.upper()
# print(op)



#print numbers from 5 to 25

# for x in range(5,26):
#     print(x)

#add the nums in b/w 5to 10

# sum=0
# for x in range(5,11):
#     # print(x)
#     sum+=x
# print(sum)

#find the factorial of given num
# ip=int(input("enter number : "))

# 5
# 5 4 3 2 1
# 1 2 3 4 5
fact=1
# for x in range(ip,0,-1):
#     # print(x)
#     fact*=x
# print(fact)

# for x in range(1,ip+1):
#     fact*=x
# print(fact)


ecommerce_data = [
    {
        "order_id": "O1001",
        "customer_name": "Ravi Kumar",
        "city": "Hyderabad",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "price": 799,
        "quantity": 2,
        "total_amount": 1598,
        "payment_method": "UPI",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1002",
        "customer_name": "Sneha Reddy",
        "city": "Bangalore",
        "product": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1999,
        "quantity": 1,
        "total_amount": 1999,
        "payment_method": "Credit Card",
        "order_status": "Shipped"
    },
    {
        "order_id": "O1003",
        "customer_name": "Arjun Singh",
        "city": "Mumbai",
        "product": "Running Shoes",
        "category": "Fashion",
        "price": 2499,
        "quantity": 1,
        "total_amount": 2499,
        "payment_method": "Cash on Delivery",
        "order_status": "Processing"
    },
    {
        "order_id": "O1004",
        "customer_name": "Priya Sharma",
        "city": "Delhi",
        "product": "Smart Watch",
        "category": "Electronics",
        "price": 3499,
        "quantity": 1,
        "total_amount": 3499,
        "payment_method": "Debit Card",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1005",
        "customer_name": "Kiran Patel",
        "city": "Chennai",
        "product": "Laptop Backpack",
        "category": "Accessories",
        "price": 1299,
        "quantity": 3,
        "total_amount": 3897,
        "payment_method": "UPI",
        "order_status": "Shipped"
    }
]

#print customer names from each dictionary from the given list
# for x in ecommerce_data:
#     print(x['customer_name'])
for x in ecommerce_data:
    if x['price']>1000:
        print(x['customer_name'])

#print customer names who is using UPI payment method 
#print customer names who is purchasing quantity more than 1
#print customer names who is purchasing other than electornics category