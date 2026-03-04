# """
# to execute set of statements in an infinite loop until it meets certain condition
# we can use while loop.
# syntax:
# while condition:
#     //statements
# it is a never ending loop, executes infinite time until condition becomes false
# """

# # while True:
# #     print('hello')


# # if True:
# #     print('hi')

# # is_recharge=True
# # while is_recharge:
# #     print('can make calls and browse internet')

# # limit=30
# # starts=1

# # while starts<=limit:
# #     print('able to make calls and browse internet')
# #     starts+=1

# # for x in range(1,31):


# """
# ott subscription based using while loop

# """

# # plan=30
# # current_day=1

# # while current_day<=plan:
# #     print(f'day - {current_day} watch and njy netflix')
# #     current_day+=1
# # print(current_day)


# str1='something'

# # x=0
# # while x<len(str1):
# #     if str1[x] in 'aeiou':
# #         print(str1[x])
# #     x+=1


# # x=len(str1)-1
# # count=0
# # while x>=0:
# #     count+=1
# #     x-=1




# # x=0-->0<9-->s-->no 
# # x=1-->1<9-->o--->o 


# # for char in str1:
# #     print(char)

# # while str1<=len(str1):
# #     print(str1)

# # for x in range(0,len(str1)):
# #     print(x)


# # num=48962
# # str1=str(num)
# # x=0
# # while x<=len(str1)-1:
# #     print(str1[x])
# #     x+=1

# # 0-->0<=4-->T=str1[0]=4 
# # 1-->1<=4-->T=str1[1]=8
# # 2-->2<=4-->T=str1[2]=9 
# # 3-->3<=4-->T=str1[3]=6 
# # 4-->4<=4-->T=str1[4]=2
# # 5-->5<=4-->Fstr1[5]=??? 


# num=158
# while num>0:
#     ld=num%10 
#     print(ld)
#     num=num//10

# 158-->158>0-->num%10--->8--->//10-->15
# 15-->15>0-->5-->//10-->1
# 1--->1>0-->1%10-->1-->//10-->0
# 0>0 F 


# num=158
# count=0
# while num>0:
#     ld=num%10 
#     # print(ld)
#     count+=1
#     num=num//10
# print(count)

#sum of the digits in given number

# num=1245
# sum=0
# while num>0:
#     ld=num%10
#     sum+=ld
#     num=num//10 
# print(sum)


# num=565
# num1=num
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld 
#     num=num//10
# print(rev)
# if rev==num1:
#     print('it is a palindrome')
# else:
#     print('it is not a palindrome')





"""
before while loop starts num=565

after 1st iteration= num=56

after 2nd iteration= num=5

after 3rd--->num=0


"""
# 0==565

"""
num=565 rev=0
num1=num

before while loop


after while loop

num= rev=565

num1=rev

"""

# write a program to check whether given num is armstrong or not 
