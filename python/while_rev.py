# """
# whenever dont know how many iterations to be done
# whenever iterations purely depends on condition
# in those cases, we will use while loop

# str="hello"
# list1=[1,2,3,4,45]

# range(1,10,2)


# but while loop we can't say whenit can be ends.
# high chances of infinite loops for while loop.

# very less chances of infinite loop in for loop


# while condition:
#     //block

# if -->executes only once if condition is true
# while-->executes continuosly until condition is in true.


# """

# # while True:
# #     print('hello')


# # while 2==2:
# #     print('hi')

# #condition should fail to stop the while loop.

# # x=1
# # while x<5:
# #     print('yes')
# #     x+=2

# # for x in range(1,5):
# #     print('yes')


# """
# in while loop--->it purely depends on condition only.
# we need to tell where to start and how to update additionally.

# but in for loop everything will comes in the part of syntax itself.
# """

# #1.count the number of digits in given number
# """
# 145--->3
# 1258--->4
# 12-->2
# """

# # x=145 #-->5
# # # x=14
# # print(x%10)
# # print(x//10)

# # x=145587
# # count=0
# # while x>0:
# #      ld=x%10
# #      count+=1
# #      x=x//10
# # print(count)



# 6--->1,2,3,4,5,
# 1,2,3,-->1+2+3=6


# 28---> 1to 28

# 1,2,4,7,14,
# =28

#find the divisors of given num
#sum of those divisors

# num=14
# x=1
# sum=0
# while x<=num//2:
#     if num%x==0:
#         print(x)
#         sum+=x
#     x+=1
# if sum==num:
#     print('it is a perfect num')
# else:
#     print('it is not a perfect number')


#perfect square logic..?


# 2=no 
# 3=no 
# 4=2**2
# 5 no 
# 6 no 
# 7 
# 8
# 9=3**2
# 10 no 
# 16=4**2

# num=15
#python logic
#15 is a ps or not


"""
10
1x1==10
2x2==10
3x3
4x4
5x5==10
10


"""
num=100
x=1
is_perfect_square=False
while x<=num//2:
    if x*x==num:
        is_perfect_square=True
    x+=1
if is_perfect_square:
    print('it is a perfect square')
else:
    print('not a perfect square')

