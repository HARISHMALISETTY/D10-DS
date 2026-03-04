# print("hello world")
# print("welcome to data science")
# print("hello")
# print("hii")
# x="""
# cdsgckhjdsabdskjc
# cdshcbdksajcdksajncdsajnc as
# chj,dsbacbdsajcndsj
# cjbdhsacbdskajxmz
# cbdsabcdskhxzdscxz
# """
# print(x)
# print("hiiii")
# print(x)

# x=""
#single variable assignment
# x="hellooo"
# y="welcome"

#multi variable assignment
x,y,z="hi","hello","welcome"
# print(x)

ip1=25
ip2=26.5
ip3='data'

#type()--->used to check the type of the data

# print(type(ip1))
# print(type(ip2))
# print(type(ip3))

#id()---->returns the memory address/id of a data/value

# ip4=12345
# print(id(ip4))

#input()--->is a method which will takes input from the user
#input method will read the value as a string
#with the help of int() we can convert from string to integer
# x1=int(input("enter value for x1  : "))
# print(x1)

# print(type(type(x1)))
# print(type(print("hellooo")))
# print(type(id(x)))


# x=print("hello world")
# y=123

# z=id(y)
#print method is just printing but not returning anything

#purpose of method--->to do something and return something(optional)

# print(x)
# print(z)

#few methods/functions may or may not return something
#if it is not returning anything then the default value will be None

# x=None

# print(type(x))

#print()--->to display output/value/data.
#if we want to display data dynamically

#print student name
# print("manohar")
# name=input("enter name : ")
# city=input("enter city : ")
# purpose=input("enter purpose : ")

# print(f"entered name is {name}")
# print("enter the name :",name)
#student came to city for the purpose

# print(f"{name} came to {city} for {purpose} purpose")
# op=f"{name} came to {city} for {purpose} purpose"
# print(op)

#frnd1 and frnd2 going to watch a movie in theatre
frnd1=input("enter friend 1 name : ")
frnd2=input("enter friend 2 name : ")
movie=input("enter movie name : ")
theatre=input("enter theatre name : ")


op=f"{frnd1} and {frnd2} are going to watch a movie {movie} in theatre {theatre}"
print(op)


"iam karan, came to hyd and joined in 10000 coders for datascience course"
