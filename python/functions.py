# """
# 1.predefined/built-in:
# functions which were defined already by python itself for certain tasks
# 2.userdefined:
# functions which can be defined by user as per his requirement then it is said to be userdefined functions
# a.static function:Function which will give always fixed output whenever we call
# b.dynamic function:Function which can give different outputs based on inputs.

# syntax:
# -------
# def func_name():
#     //code

# func_name()--->like this we can invoke/call a function
# BY default a function can return None as a value.
# to return any value specifically we can use return
# the code what we write after the return statements, they won't executes.simply will ignore


# dynamic functions:
# ---------------
# def dynamic(x,y,z): //parameters
#     print(x+y+z)

# dynamic(2,4,6) //arguments

# types in dynamic functions
# 1.positional arguements-->always count and positions of params and args should be match


# """

# # def sample():
# #     print('hello iam a sample function')
# #     return 'thankyou'
# #     print('visit once again')
# # print(sample())

# #thankyou is being returnd by sample()(func def)
# #and assigning into the function call sample()




# #to say hello for a student using a function as per his name


# # def greetings(name):
# #     print(f"hello {name}")
# #     return '10000-coders'

# # print(greetings('kishore'))
# # print(greetings('ashok'))
# # greetings('kiran')
# # print(greetings('hemanth'))



# # def showtime(name,movie):
# #     print(f"{name} is watching {movie}")
# #     return 'Thankyou for visiting us'

# #this function is returning a value thankyou for visting us

# # showtime('madhu','OG')
# # print(showtime('kiran','edokati'))

# # showtime('john','')


# #write a function  to calculate the movie tickets
# def movie_tickets(price,quantity):
#     return 'welcome'
#     total=price*quantity
#     print(f"total amount is {total}")
#     return 'thankyou visit again'

# movie_tickets(200,3)
# # print(movie_tickets(int(input('enter ticket price : ')),int(input('enter no.of tickets : '))))

# #write a function which calculates movie tickets price and returns
# #gift as per billing amount
# #if amount is greater than 2000 then return coke+popcorn
# #if amount id greater than 1500 then return coke
# #if amount is less than 1500 then say thankyou


# def sample():
#     print('hello')
#     print('welcome')
#     print('d10')
#     return 'bye'

# print(sample())
# print(sample())


# def dynamic(a,b):
#     print(a,b)

# dynamic(10,20)
# dynamic('hello','welcome')
# dynamic(123,'okokok')

def city_details(state,city):
    print(f"{city} is in state of {state}")

# city_details('TS','Hyd')
# city_details('karnataka','bnglr')
# city_details('guntur','AP')


# def student_info(sname,degree):
#     print(f"{sname} is pursuuing {degree}")

# # student_info('karthik','b.tech')
# # student_info('b.com','gouthami')

# # 1.positional arguements-->always positions of params and args to be match here.

# # 2.key-word arguements-->we use this when we don't know the sequence or positions of args if we dont know.

# # 3.arbitray args(*args)-->when we don't know exact count of args then we can use arbitrary args (*params).
#here all arguments can be assigned in the form of tuple to the param
# student_info(degree='b.tech',sname='shiva')

# 4.keyword-arbitray arg(**args)-->here n numb of arguments can be pass with there keywords.
#and args can be assigned as dictionary.

# 5. default parameter:whenever value is fixed /default we can use default param
#   always default param should be end of the params
#   we can overwrite the default param.
# def demo(*ip):
#     print(ip[1])

# demo(1,2,3,4)
# demo('soap','shampoo','deodrant','snacks')
# demo('chicken','mutton')


# def demo1(**ip1):
#     print(ip1['first'])

# demo1(first='ram',third='bharath',second='lakshman')


# def student_info1(sname,city,batch='d10',institue='10000coders'):
#     print(f"{sname} is from {city} in batch {batch} from {institue}")

# student_info1('shiva','hyd')
# student_info1('karthik','warangal','d11')



# def sum(a,b):
#     print(a+b)
#     return 'something'
#     print('hellooo') #this will never execute
    

# x=sum(3,4)
# print(x)



#write a funtion that returns the length of given object


# def find_length(ip):
#     op=len(ip)
#     return op 
# print(find_length('hello world'))
# find_length('something')
# find_length([1,2,3,4])
# find_length((4,5,6,7))





"""
1.using a function find the length of the given input without using len method

"""


# def find_length(x):    
#     count=0
#     for i in x:
#         count+=1
#     return count

# print(find_length('hello'))
# print(find_length('welcome'))
# print(find_length([1,2,3,4]))
# print(find_length(('hi',4,8,'ok')))


# x=123
# print(isinstance(x,list))

def find_length1(x):
    count=0
    if isinstance(x,int):
        print('given input is integer')
        while x>0:           
            count+=1
            x=x//10
        print(count)
    else:
        print('given input is not an integer')
        for i in x:
            count+=1
        print(count)
# find_length1(123)
# find_length1([1,2,3])
# find_length1('hello')
# find_length1((4,6,8,9))

# print(isinstance([1,2,3],list))

#write a function to check whether given input is palindrome or not

def palindrome(x):
    if isinstance(x,int):
        rev=0
        temp=x
        while x>0:
            ld=x%10 #3,2,1
            rev=rev*10+ld #0*10+3-->3,3*10+2-->32--> 32*10+1-->321
            x=x//10 #-->12,1,0
        if rev==temp:
            print('it is a palindrome')
        else:
            print('it is not a palindrome')
    elif isinstance(x,str):
        rev=""
        for char in range(len(x)-1,-1,-1):
            rev+=x[char] 
        if rev==x:
            print('it is a palindrome')
        else:
            print('it is not a palindrome')
    else:
        print('only integers or strings allowed')    

palindrome(121)
palindrome('level')
palindrome('markram')

#implement logics for perfect number and perfect square using functions

def fun1():
    print('iam function1'):

fun1()
fun1('hello')