"""
simple-if
if-else
if-elif-elif-else
nested-if
"""

# print("statement1")
# if 2==3:
#     print("statement2")
#     print("statement3")

"""
1.take a number and check whether it is
a positive or negative
"""
# num=int(input("enter the number : "))

# if num<0:
#     print('it is negative')
# else:
#     print('it is positive')

# if num==0:
#     print('number is zero')
# elif num<0:
#     print('number is negative')
# elif num>0:
#     print('number is positive')
# else:
#     print('invalid number')



# a=25
# b=120
# if a>b:
#     print('a is largest')
# else:
#     print('b is largest')




# if a>b and a>c:
#     print('a is largest',a)
# elif b>a and b>c:
#     print('b is largest',b)
# else:
#     print('c is largest',c)


# if a<b and a<c:
#     print('a is smallest',a)
# elif b<a and b<c:
#     print('b is smallest',b)
# else:
#     print('c is smallest',c)


#check whether given num is 2-digit or not.

# 789--->its not a 2 digit 
# 78-->its a 2 digit
# >9 and <100 

# --->12 -->2 digit 
# -->123--->3 digit 
# --->1254--->4 digit 
# --->1214541-->more than 4 digit 

# num=int(input('enter the number : '))
# if num<9 and num>0:
#     print('single digit')
# elif num>9 and num<=99:
#     print('two digit')
# elif num>=100 and num <=999:
#     print('3 digit')
# else:
#     print('more than 3 digit')


# num=int(input('enter the number : '))
# if num<0:
#     print('it is negative')
# elif num<9 :
#     print('single digit')
# elif num<=99 :
#     print('two digit')
# elif num<=999 :
#     print('3 digit')
# else:
#     print('more than 3 digit')

#check whether num is leap year or not
#generate electricity bill as per the units
"""
for first 100 units--->2rs/unit
next 100 units--->3rs/unit
above 200 units-->5rs unit

"""

"""
1.should divisible by 400
2.should not divisible by 100
3.should divisible by 4
"""
# 

# year=2025
# if year%400==0:
#     print('it is a leap year')
# elif year%100==0:
#     print('it is not a leap year')
# elif year%4==0:
#     print('it is a leap year')
# else:
#     print('it is not a leap year')

# if (year%400==0) or (year%100!=0 and year%4==0):
#     print('it is a leap year')
# else:
#     print('not a leap year')

# units=int(input('enter the units : '))
# total_amount=0

# if units<=100:
#     total_amount=units*2
#     print(f'your bill is {total_amount} ')
# elif units<=200:
#     total_amount=(units-100)*3+100*2
#     print(f'your bill is {total_amount} ')
# else:
#     total_amount=(units-200)*5+100*2+100*3
#     print(f"ur bill is {total_amount}")

# v1=int(input("enter a value : "))
# v2=int(input("enter a value : "))
# v3=int(input("enter a value : "))

# if v1+v2+v3==180:
#     if v1==v2==v3:
#         print('equilateral triangle')
#     elif v1==v2 or v2==v3 or v3==v1:
#         print('isosceles triangle')
#     else:
#         print('scalene triangle')
# else:
#     print('can not form a valid triangle')


"""
using nested if

temp is less than zero--->its freezing

temp is greater than zero--->
    --->temp less than 30--->moderate
    --->temp greater than 30-->its so hot
"""


# temp=int(input('enter temperature : '))
# if temp>0:
#     if temp<30:
#         print('it is moderate')
#     else:
#         print('it is so hot')
# else:
#     print('it is freezing')


"""
if we watch devara-1 then only we can watch devara-2
otherwise go and watch devara-1
"""

# is_devara1_watched=True 
# is_devara2_released=True 

# if is_devara1_watched:
#     if is_devara2_released:
#         print('u can watch devara-2')
#     else:
#         print('wait until devara-2 release')
# else:
#     print('go and watch devara-1')

