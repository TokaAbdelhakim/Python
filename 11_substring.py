user_string = input("Enter your string: ")

def subString (user_string):
    current_string = user_string[0]
    longest_string = user_string[0]

    for c in  user_string[1:]:
        if c >= current_string[-1]:
            current_string += c 

            if len(current_string)> len(longest_string) :
                longest_string = current_string               
        else:
            current_string = c

        if len(current_string) == len(longest_string) :
             i = 0            
             for l in longest_string[0:]:
                if l >= current_string[i]:
                     longest_string = current_string
                     i+=1
            
    return longest_string

print ('Substring: ' + subString(user_string))

