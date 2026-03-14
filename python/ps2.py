# # """
# # lst=[[1,2,3],[3,4,5],[2,1,3]]
# # """
# # lst=[[1,2,3,4,6,],[3,4,5,1],[2,1,3,6,7],[3,4,5]]

# # dct={}
# # for x in range(len(lst)):
# #     sum=0
# #     for y in lst[x]:
# #         sum+=y
# #         dct[x]=sum
# # print(dct)

# # max=0
# # for i in dct:
# #     if dct[i]>max:
# #         max=dct[i]
# #         ind=i
# # print(max,ind)

# # print(f'max amount of list is {lst[ind]}')


# lst=[1,2,3,3,2,14,5,4,5,7]
# dct1={}
# for x in lst:
#     if x in dct1:
#         dct1[x]+=1
#     else:
#         dct1[x]=1
# print(dct1)
# dup=[]
# for i in dct1:
#     if dct1[i]>1:
#         dup.append(i)
# print(dup)



# # op=[2,3,5]

# # {1:1,2:2,3:2,14:1,5:2,4:1,7:1}

# # iterate this dict and push the keys which are having values
# # greater than 1.

sentence='python is a very powerful programming language'

# op=['python','is','a','very','powerful','programming','langugage']
word=''
lst=[]
for i in sentence:
    if i !=' ':
        word+=i 
    else:
        lst.append(word)
        word=''
lst.append(word)
print(lst)

ip='aaabcccdde'

#find first non-repeating character from the given input string
    
# i=py
# word=python 

# lst=['python']
# word=''

# i=i 

# word=is 

# lst=['python','is']
# word=''

# i=a 

# word=a 

# lst=['python','is','a']
# word=''

# word='language'

# l