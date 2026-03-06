"""
looping statements:
------------------
statements which executes continuosly in a loop until it meets certain condition.

we have 2 types of loops in python mainly
1.for loop
a.whenever if u want to use loop for the sequence type data we can use one type of for loop
    syntax:
    -------
            for var in seq:
                //statements
b.whenever if u want to use loop as per our own count we can use one type of for loop
    syntax:
    -------
        for var in range(start,end,step):
            //statements

by default step value will be one

2.while loop

"""


str1="data science"
# print(str1[0])
# print(str1[1])
# for char in str1:
#     print(char)

# list1=['hi','hello','some','welcome','thankyou']

# for element in list1:
#     print(element[0])


# dict1={'name':'harish','city':'hyd','role':'develoepr'}

# print(dict1['name'])
# for x in dict1:
#     print(dict1[x])

# print(dict1)

# for x in dict1:
#     print(f"{x} :{dict1[x]}")

#by default loops starts at zeroth index of the string
#and ends at end of the string
#it means iterates throughout the length of the string/seq

# set1={'karun','kiran','shiva','yamini','sahasra','mounika'}
# for name in set1:
#     print(name)


#to print numbers from 1 to 10

# for x in range(1,11,3):
#     print(x)
#so here x is taking every value from range

# #to print numbers from 20 to 30
# for x in range(20,31):
#     print(x)

# #print squares of numbers from 10 to 30
# for x in range(10,31):
#     print(x**2)

#WAP to print multiplication table of given num

# 2x1=2 
# 2x2=4

# for x in range(1,11):
#     print(f"3 x {x} = {3*x}")

# for x in range(10,0,-1):
#     print(x)


list1=[10,23,45,31,24,67,87,45,34,'hi','hello']

# for x in range(len(list1)-1,-1,-1):
#     print(x)

# list1 length=5--->len(list1)-
# list2 length=8--->len(list2)-1,-
# for x in list1:
#     print(x)

#print values from the list within indeces of 3rd to 7th

# for x in range(3,8):
#     print(list1[x])

#print elements from the list in reverse

# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])

#to print multiplication table in reverse

# for x in range(10,0,-1):
#     print(f"4 x {x}={4*x}")

# names=['karun','kiran','shiva','yamini','sahasra','mounika']
#print only even length names
# for name in names:
#     if len(name)%2!=0:
#         print(name)


# for name in names:
#     if len(name)%2==0:
#         print(f"{name}- even")
#     else:
#         print(f"{name} - odd")

# #print numbers from 1 to 20 
# if num is divisible by 3 then print num-fizz
# if num is divisible by 5 then print num-buzz
# if num is divisible by both then print num-fizzbuzz


# for x in range(1,21):
#     if x%3==0 and x%5==0:
#         print(f"{x}-Fizz Buzz")
#     elif x%5==0:
#         print(f"{x}-buzz")
#     elif x%3==0:
#         print(f"{x}-fizz")
#     else:
#         print(x)

# list1=[10,23,45,31,24,67,87,45,34]
# x=1
# for num in list1:
#     print(x+num)
#     x+=1
   
#from numbers 1 to 50 count howmany can be divisible by 3 and 5

# count=0
# for i in range(1,51):
#     if i%3==0 or i%5==0:
#         count+=1
#         print(i)
# print(count)

# i=1--->3or5-->F count=0
# i=2--->3or5-->F count=0
# i=3--->3 or 5-->T count=3
# i=4-->3or5-->F count=3
# i=5-->3or5-->T-->8


"""from 1 to 30
add even numbers
and multiply odd numbers using for loop
"""

# sum of all even numbers=85 
# product of all odd numbers=1200
# sum1=0
# prod=1
# for x in range(1,31):
#     if x%2==0:
#         sum1+=x        
#     else:
#         prod*=x
# print(f"sum of the even numbers are :{sum1}")
# print(f"product of the odd numbers are :{prod}")
# 1--->1
# 2--->2


for x in range(3):
    print('hello')