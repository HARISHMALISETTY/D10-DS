"""
statements:
1.normal--->statements which executes normally without depends on any condition or decisions.
2.conditional-->statements which executes on conditional based or decision based
a.simple-if
syntax: if condition:
            //statements or True/if block
b.if-else
syntax: if condition:
            //statements or true/if block
        else:
            //statements or false/else block


c.if-elif-else
    if condition1:
        // true/if block
    elif condition2:
        //elif/alternate true block
    elif condition3:
        //elif/alternate true block
    else:
        //final false block
d.nested-if:
    syntax: if condition1:
                //true block
                if condition 1.1:
                    //true 1.1 block
                else:
                    //false block for condition 1.1 
            else:
                //false block for condition 1

3.looping--->statements which executes in a loop based on condition.
a.for loop
b.while loop

"""
# false=4
# print('statement1')
# print('statement2')
# if -10:
#     print('statement3')
# print('statement4')

# password=5
# if password:
#     print('password is correct')

#whenever we have only one condition and one outcome then we have to use simple-if
#whenever we have one condition but 2 outcomes then we have to use if-else

# is_verified=True
# if is_verified:
#     print('add blue tick to the profile')
# else:
#     print('no blue tick to the profile')



# is_verified=True
# if is_verified:
#     print('add blue tick to the profile')
# else:
#     print('no blue tick to the profile')

# # True --->boolen value 
# # true--->variable name 
# # 'true'--->string value    

# 1.if two users are frnds in instagram then they can send message to each other.
# 2.if not need to become frnds to send messages


# are_friends=False 
# if are_friends:
#     print("can send messages to each other")
# else:
#     print("need to become frnds to send messages")

# status=True
# if status=='ordered':
#     print('u have placed a new order')
# elif status=='confirmed':
#     print('ur order is confirmed')
# elif status=='pending':
#     print('ur order is still in pending')
# elif status=='delivered':
#     print('ur order is delivered')
# else:
#     print('invalid status')


#if student knows db,b.e and f.e--->fullstack
#b.e-->backend dev
#f.e--->frontend
#d.b-->database dev
#go and join in 10000coders


frontend=True
backend=True
db=True

if frontend and backend and db:
    print('become a FSD')
elif frontend and backend:
    print('become wither frontend dev or b.e dev')
elif frontend and db:
    print('becomd f.e along with db skills')
elif backend and db:
    print('becomd b.e along with db skills')
elif frontend:
    print('become f.dev')
elif backend:
    print('becomd b.dev')
elif db:
    print('become dbdev')
else:
    print('go and join in 10000coders')


#if two users are frns then they can send messages
#if  not then 
    # check for account privacy-->if account is public then send message 
    #                         ---> if not can not send message
# using nested if 

are_friends=True
is_account_public=True
allow_everyone=False

if are_friends:
    print("both can send messages")
else:
    if is_account_public:
        if allow_everyone:
            print("send messages without becoming frns")
        else:
            print("only frnds can send message")
    else:
        print("can not send message until they become frns")