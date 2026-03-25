"""
a thing calling itself is called recursion.

harish is calling harish-->recursive harish

vehicle is calling vehicle only-->recurive vehicle

function is calling that function itself-->recursive function.


A function is being called by itself is called recursive function. and that process
can be called as recursion.

so, here this recursion can be happened upto certain condition.

otherwise this will be happens in infinite loop.


if we dont add any condition, this recursion can be happened approx 1000 times which leads
unnecessary function calls.





"""


# def sample():
#     print('hello')
#     sample()
# sample()

# def openbox(box):
#     if box!=0:
#         print(f"{box} box opened")
#         return openbox(box-1)
#     print('gift found')
# openbox(5)



# def climb(steps):
#     if steps>=0:
#         print(f"climbed {steps} steps")
#         return climb(steps-1)
#     print('reached first floor')  

# climb(6)

# def climb(steps):
#     for x in range(steps,-1,-1):
#         print(f"{x} steps climbed")
#     else:
#         print("reached first floor")
# climb(6)


    
# box-->5= 5th box opened,openbox(5-1)
# box-->4=4th box opened, openbox(4-1)
# box-->3=3rd box opened, openbox(3-1)

"""
if we use recursion, it will leads to more space complexity and time
complexity.

so we preffer loops than recursion for repetetion process
"""

"""
print numbers from 5 to 1 using recursion
"""

# def numbers(ip):
#     if ip>=1:
#         print(ip)
#         return numbers(ip-1)
#     print('hello')
# numbers(5)

"""
add numbers from 5 to 1

ip-->5 then op-->15
ip-->10 then op-->?
"""


# def numbers(ip,sum):
#     if ip>=1:
#         sum+=ip
#         return numbers(ip-1,sum)
#     print(sum)
    
# numbers(5,0)


def factrial(ip,fact):
    if ip>=1:
        fact*=ip
        return factrial(ip-1,fact)
    print(fact)
factrial(5,1)






