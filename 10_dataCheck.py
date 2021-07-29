import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
name = input("Enter your name: ")

if not name or name.isdecimal():
    print("please enter valid name")
else:
    email = input("Enter your email: ")
    if(re.match(regex, email)):     
        print ("Name is:", end="")
        print (name)
        print ("Email is:", end="")
        print (email)
    else:
        print("please enter valid email")
