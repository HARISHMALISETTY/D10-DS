"""
identity operators:
------------------
whenever two values are same , to check whether their ids are same or different
we can use these identity operators.

is and isnot

"""

# x=289
# y=289
# print(x is y)


# x=[1,2,3]
# y=[1,2,3]
# print(x is not y)
# #in not in
# str1="hello world"
# print('x' not in str1)

# list1={1,2,3,7,8}
# print(2 not  in list1)

# ds_course=['python','sql','excel','powerbi','ML','AI','DS']

# print('javascript' not in ds_course)

# dict1={'name':'kiran','city':'hyd','gender':'male','age':25}

# print('male' in dict1)

#if any values u want is not available in given sequence, we can check
#them using membership operator and we can add them if required

"""
bitwise operartors:
-----------------
and(&),or(|),not(~),xor(^),ls(<<),rs(>>)

^ gives 1 if both are different
"""

# print(bin(5))
# print(bin(25))

# print(5 & 11)
# print(5 | 11)
# print(~6)
# print(~10)
# print(~0)
# print(~-5)
#formula for ~n--->-(n+1)
# -(-5+1)
# -(-4)
# 4
# print(4 ^ 5)

"""
left shift--> number << shiftcount

shift the bits shiftcount times towards left

right shift--->number >> shiftcount
shifts the bits shiftcount times towards rightside
"""

# print(5 << 3)
# print(bin(40))


# print(4 << 2)

# 00000100<<2


# print(6 >> 3)

"""
terinary operator:
------------------
x=10
assigning value to the variable based on condition , we can use terinary operator.
x=value1 if True else value2
"""
# time=16
# x='gudevg' if time > 18 else 'gudaftn'
# print(x)


# is_data_cleaned=False
# # type1="LIST" if not is_data_cleaned else "TUPLE"
# type1='tuple' if is_data_cleaned else 'list'
# print(type1)


# x=5 if 6>7 else 4
# x=5 if False else 4
# x=4

# x=5 if True else 4
# x=5 if [] else 4

# print(x)

# stored_password='INDIA@123' 
# stored_username='INDIAN'
# input_username=input('enter username : ')
# input_password=input('enter password : ')

# login_status='succefully logedin' if (input_password==stored_password and input_username == stored_username) else 'invalid credentials'
# print(login_status)

#write a program to check whether given num is positive or negative using terinary operator

# num=int(input("enter the number : "))
# op='positive' if num >0 else 'negative'
# print(op)

#check whether given num is even or odd using bitwise operator and terinary but not %


# num=int(input('enter any number : '))
# # op='even' if num%2==0 else 'odd'
# op='even' if num & 1==0 else 'odd'
# print(op)


