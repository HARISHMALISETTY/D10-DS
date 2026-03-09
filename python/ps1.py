"""
***
***
***

"""

# for y in range(3):
#     for x in range(3):
#         print('*',end=' ')
#     print()

# y=0-->x=0-->'*'
#       x=1-->'*'
#       x=2-->'*'
# y=1-->x=0-->'*'
#       x=1-->'*'
#       x=2-->'*'
# y=2-->x=0-->'*'
#       x=1-->'*'
#       x=2-->'*'

# for y in range(3):
#     for x in range(1,4):
#         print(x,end=' ')
#     print()

# for y in range(1,4):
#     for x in range(1,4):
#         print(y,end=' ')
#     print()

"""
a b c
a b c
a b c
"""

for y in range(3):
    for x in range(3):
        print(chr(x+97),end=' ')
    print()


# y-->1
#     x=0-->1
#     x=1--->2
#     x=2---3

# y-->2

#     x=0--->2 3 4
#     x=1
#     x=2

# y--->3
#     x=0-->3 4 5
#     x=1
#     x=2
"""
123
234
345

"""
"""
abc
bcd
cde

ABC
BCD
CDE
"""