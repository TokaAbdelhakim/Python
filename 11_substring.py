user_string = input("Enter your string: ")

def subString (user_string):
    current_string = user_string[0]
    longest_string = user_string[0]

    for c in  user_string[1:]:
        if c >= current_string [-1]:
            current_string = current_string + c 
            print (current_string)
            if len(current_string)>= len(longest_string) :
                longest_string = current_string
        else:
            current_string = c
        return longest_string

print (subString(user_string))

