"""
1.arithematic--->+,-,*,/,%,//,**
2.assignment-->=,+=,-=,/=,%=,//=,*=,**=
3.logical--->AND,OR,NOT
4.relational/comparision-->==,!=,<,>,<=,>=
5.identity--->is, is not
6.membership--->in, not in
7.bitwise--->and,or,xor,not,<<,>>
8.terinary operator-->else if
"""

x=12
y=13
# print(x+y)
#+-->operator
#x and y are operands
#x+y is operation

# print('hello'+'world')
# print(2+'hello') #unsupported for one string and one number

# print(2+7j+4+8j)
# print(2+7j+4)

# print(5-4)
# print('hello'-'world')

# print(5*2)
# # print('hello'*2)
# print(5/2) #returns quotient in float completely
# print(5//2) #returns quotient but only gives integer part only by ignoring decimal values
# print(5%2) #returns reminder
# print(4**2)  #means 4 power of 2
# print(2**6) #means 2 power of 6


#assignment operators

x=123 #just assigning value
# +=this will add the value and assign
# a=125
# a=a+2 #adding 2 into the a and assigning it to a only
# a+=2

#a=a+2 is same as a+=2

# a=12 #12
# a+=3 #15
# print(a)
# a-=3 #12
# print(a)
# a*=2
# print(a)
# a/=3
# print(a)
# a**=2
# print(a) #a=64.0
# a%=3
# print(a) #1.0

# b=7.0
# b%=5
# print(b)

#truth values
#True,125,-125,

#falsy values
# False,0,"",None,[],()

# #and
# print(True and True)
# print(True and False)
# print(False and False)
# print(False and True)
# print(125 and True)
# print("" and True)
# print(0 and True)
# print(0 and 0)
# print(-1 and 2)
# #and operation b/w two truth values gives the second truth value
# print(2 and 4)
# print("" and 0)
# #and operation b/w two falsy values gives the first falsy value 
# print(None and 4)
# print([]and())
# print([1,2] and (2,4))



# print(True or True)
# print(True or False)
# print(False or False)
# print(False or True)
# print(1 or 0)
# print(0 or 0)

# print(not True)
# print(not False)
# print(not [1,2] and (2,4))
# print(not 5)
# print(not "")
# print(not -234)

#if we gives not for truth values-->false
#if we gives not for falsy values-->true

"""
relational/comparision--->

whenever if we want to check relation between values we can use this
==
!=
<,>,<=,>=
"""

print(4==4)
print(123!=123)
print([1,2,3]!=[1,2,3])
print('hello'=='hello')

print((1==1)and(2==2))
# <,>,<=,>=

# identity operator 

# is ,is not
#this will check the id of two values
#if two ids are same then gives true otherwise false

print(4 is 4) #4 and 4 are having same id
print([1,2,3] is not [1,2,3])

#== is 

# ==
# =

