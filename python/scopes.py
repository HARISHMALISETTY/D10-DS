"""
scope:->life of a variable through out the program is nothing but its scope.

L-E-G-B

LOCAL-->variable which declared inside a function is having local scope.
ENCLOSED--->variable which declared inside nested function is having enclosed scope.
GLOBAL--->variable which declares globally in the program is having global scope
BUILTIN--->All the builtin methods will be having builtin scope
"""
# hero='MAHESH BABU' #declared globally, so it is having global scope.
# def tollywood():
#     print('iam tollywood')
#     print(hero)
# def bollywood():
#     print('iam bollywood')
#     print(hero)
# def sandalwood():
#     print('iam sandalwood')
#     print(hero)
# def kollywood():
#     print('iam kollywood')
#     print(hero)
# def hollywood():
#     print('iam hollywood')
#     print(hero)
# tollywood()
# bollywood()
# kollywood()
# sandalwood()
# hollywood()

# def tollywood():
#     hero_t='viswak' #local variable
#     print(hero_t)
# def bollywood():
#     hero_b='shahidh' #local variable
#     print(hero_b)
#     print(hero_t) #cannot access here because it is local to tollywood
# def hollywood():
#     hero_h='james'
#     print(hero_h) #it is local to hollywood

# tollywood()
# bollywood()
# hollywood()


def pspk():
    son='akhira'
    def tollywood():
        print(son)
        x=4
    def bollywood():
        print(son)
        y=5
    tollywood()
    bollywood()


"""
son is having enclosed scope in pspk function
can access from tollywood and bollywood
"""

# pspk()


"""
to modify the scope of a variable we have 2 scope
modifiers
1.global
2.nonlocal


"""

x=125 #global variable

# def sample():
#     global x
#     x=2 #global variable x is changing from function
#     print(x+5)
# sample()

# print(x+10)

# print(x+10)

"""
to change global variable from a function 
we can access that variable inside a function
using global keyword
"""
x=85
def demo():
    global x
    x='hello'
    print(x)
# demo()
# print(x)

"""
to change variable of outerfunction
from innerfunction which is having enclosed scope,
we can use nonlocal keyword
"""

def outer():
    ip='welcome'
    def inner():
        ip='something'        
        print(ip)
    inner()
    print(ip)
# outer()

# x=125
# def outer():
#     y=12
#     def inner():
#         global x
#         x='hi'
#         nonlocal y
#         y='hello'
#         print(x,y)
#     inner()
#     print(y)
# outer()
# print(x)


# def inner1():
#     global a
#     a=125
#     print(a)
# def inner2():
#     print(a)
# inner1()
# inner2()

# print(a)

def outer():
    ip='hello'
    def inner():
        global ip
        ip='something'
        print(ip)
    inner()
    print(ip)
outer()
print(ip)