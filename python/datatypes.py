"""
datatype---?
-----------
type of data/value/information which we use for doing operations/manipulations/storage purpose.
based on data read
1.Numbertype--->int,float and complex
2.texttype--->string
3.sequencetype--->list,tuple,set,dictionary
4.booleantype--->bool
5.Nonetype--->None

based on how data stores
1.primitive--->int,float,complex,string,None,bool
2.non-primitive--->list,tuple,sets,dictionary


to check type of data-->type()

1,2,3,4,
45.90
4+7j
a+bj
string-->group of characters which will write by enclosing with
'' or ""

"""

# x=12
# print(type(x))
# y=12.5
# print(type(y))
# z=3+6j
# print(type(z))

# str1="data  science" #creating string
# print(str1) #reading string
# print(type(str1))
#to find the length of the string
#supports both +ve and -ve indexing
#+ve starts from zero
#-ve starts from -1

# print(len(str1))
#len method is finds the length and returns the same
# print(op)
# print(str1[6]) #accessing specific character from the string


# print(str1[-3])
#sequence type
#list-->it is an ordered collection of values which are seperated by commas
# and enclosing with []

#a specific index for every values in the list

# list1=[1,2,'hi','hello',3.4,[12,23,34]] #creating list
# #data in the list can be heterogeneous
# # print(list1) #reading list
# # print(len(list1)) #length of the list
# # print(list1[3]) #accessing specific value in the list in +ve indexing
# # print(list1[-3]) #accessing specific value in the list in -ve indexing
# # print(list1[3][1]) #accessing specific value from the nested list
# #to print 23
# print(list1[5][1])
# print(list1[-1][-2])

# num=12540
# num1=str(num)
# print(num1)
# print(type(num1))
# print(num1[2])
# list1[3]="welcome" #updating
# print(list1)
# del list1[2] #deleting value from the list1
# print(list1)
# del list1 #deleting entire list1
# print(list1)
# CREATE,READ,UPDATE,DELETE can be done for list
#when we need to update the data in future then we need to use list only.
#but lists consumes more memory and less performance compared to tuple
#because of its changable feature(mutable) its consumes more memory.

"""
tuple:
will stores an ordered collection of value which may be different or same types and enclosed with ()

"""
# tupl1=(1,2,3.4,'hello')
# print(tupl1)
# print(type(tupl1))
# print(tupl1[2])
# print(tupl1[-1])
# tupl1[3]='welcome' #updating is not supports in tuple
# del tupl1[2] #cannot delete specific element in the tuple
# del tupl1 #entire tuple can be deleted.

# create,read, update(Not),delete (entire tuple can be)

# list1=[1,2,3]
# tuple1=(1,2,3)
# print(list1.__sizeof__())
# print(tuple1.__sizeof__())

"""
set--->stores the values in unordered  random collection but no duplicates allowed in sets
{} used to denote
allows heterogenous values
set will stores values by its hashing values
for numbers, number itself hashingvalue in most of the cases
for string, generates hashingvalue from -infinity to +infinity
hashing is the process involved in storing some secured data and
sensitive data which should not expose openly.
"""
set1={3,4,'hi','hello',5.6,4,'hi'}
# print(set1)
# print(set1[2]) #noorder means no index supports

set2={101,42,23,14,500,81,9,10,6,2,3}
# print(set2)

#sets will generates hashing values for every element in them

# print(hash(101))
# print(hash('hello'))

#hashing is the process used for securing data.

"""
dictionaries:
to store a complete information of a particular thing/object we can use dictionary
denotes with {} but contains information as key-value pairs seperates with commas.
we can access specifici information with their keys but not indexes
keys always in string formats

"apple"--->
"kiran"
"""
#create a dict which stores info of apple-->color,price,validity
# apple_info={
#             "color":"red",
#             "price":75,
#             "validity":"one week",
#             "price":85
#             }
# print(apple_info)
# print(apple_info["price"])
# print(apple_info["validity"])

#will add origin as a new information in the dict
#with new key
# apple_info["origin"]="shimla"
# print(apple_info)
# del apple_info["price"]
# print(apple_info)

#int,float,string,list,tuple,set,dictionary.

#bool,none
"""
bool: it is one of the datatype which stores boolean values like true or false.
means-->if any value is present/is able to do/is coming/..???
True or False

"""

is_pursuing_Btech=True
is_Tickets_available=True #conveying something
tickets=True #not conveying anything
job=True
is_working=True
is_working=False 

print(type(is_working))

#when data is cleaned then i can use for making reports
#otherwise i can't use for making reports
# is_data_cleaned=True 


x=None 
print(type(x))


#to make empty values for the variables without giving/assigning any values
# #in those case we can give None
# x=4
# print(x)

"""
primitive--->
if one data/value is assigned to single variable then they are primitives.
immutable at the same place/object/memory
int,float,complex,string,bool,None
non-primitive--->
if we are able to assign multiple values at a time to single variable then it is non-primitive.
these are mutable at the same place but tuples are immutable completely
list,tuples,set,dictionary.
"""
# x=125 #assigning
# print(id(x))
# x=256 #re-assingning
# print(x)
# print(id(x))

# x=[1,2,3]
# print(id(x))
# x[1]='hello'
# print(id(x))


# x='hello'

#replace e with a
# x[1]='a' #this will not supports in python for string
# print(x)

# y=[1,2,3]

# y[1]='hello'
# print(y)
#m=primitives are non primitives will stores in heap memory


# tuples are immutable

# x=456
# x=123

# x=2